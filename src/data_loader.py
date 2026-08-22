import os
import re
import numpy as np
import pandas as pd
import glob


class DataLoader:
    def __init__(
        self, data_dir="../data", labels_filename="labels.csv", signal_folder="MI CSV"
    ):
        self.data_dir = data_dir
        self.labels_path = os.path.join(data_dir, labels_filename)
        self.signals_dir = os.path.join(data_dir, signal_folder)
        self.df_labels = None
        self.valid_manifest = None
        self.load_and_align_manifest()

    def _extract_id(self, val):
        """for getting the numeric order digit from the csv file name"""
        if not os.path.exists(self.labels_path):
            raise FileNotFoundError(f"Labels file not found at {self.labels_path}")
        if not os.path.exists(self.signals_dir):
            raise FileNotFoundError(
                f"Signals directory not found at {self.signals_dir}"
            )

        filename = os.path.basename(val)
        match = re.match(r"cellula_MI_data_(\d+)\.csv$",filename)
        if match is None:
            raise ValueError(f"Filename does not match expected pattern: {filename}")

        return int(match.group(1))  

    def load_and_align_manifest(self):
        """ linking each EEG signal with it's label"""
        if not os.path.exists(self.labels_path):
            raise FileNotFoundError(f"Labels file not found at {self.labels_path}")

        if not os.path.exists(self.signals_dir):
            raise FileNotFoundError(
                f"Signals directory not found at {self.signals_dir}"
            )

        df_labels = pd.read_csv(self.labels_path)

        df_labels.columns = ["label"]

        # Get all CSV files in the signals directory
        signal_files = glob.glob(os.path.join(self.signals_dir, "*.csv"))
        print(f"Found {len(signal_files)} signal files in {self.signals_dir}")
        if len(signal_files) == 0:
            raise FileNotFoundError(
                f"No CSV files found in signals directory: {self.signals_dir}"
            )

        signal_files = sorted(signal_files, key=self._extract_id)

        n_labels = len(df_labels)
        n_signals = len(signal_files)

        print(f"[DataLoader] found {n_labels} labels and {n_signals} signal files.")

        if n_labels < n_signals:
            raise ValueError("cannot align")

        if n_labels > n_signals:
            dropped = n_labels - n_signals
            print(f"DataLoader: Dropping last {dropped} extra labels to align with signal files.")
            # filter the labels to match the number of signal files
            df_labels = (df_labels.iloc[:n_signals]).reset_index(drop=True)
            # clean labels
            df_labels["label"] = (df_labels["label"].astype(str).str.strip().str.lower())

            valid_labels = {"left","right"}

            unexpected_labels = set(df_labels["label"]) - valid_labels

            if unexpected_labels:
                raise ValueError(f"Unexpected labels found: {unexpected_labels}")

            # finally , store the aligned manifest
            manifest = pd.DataFrame({
                "trial_id": [
                    self._extract_id(file_path) for file_path in signal_files
                ],
                "file_path": signal_files,
                "label": df_labels["label"].values
            })
            self.df_labels = df_labels
            self.valid_manifest = manifest
            print(
                f"[DataLoader] successfully aligned "
                f"{len(manifest)} EEG trials with labels."
            )

            return manifest

    def load_trial(self,index):
            """ Load a single trial by index from the aligned manifest."""

            if self.valid_manifest is None:
                raise RuntimeError(
                    "Manifest not loaded."
                )

            if index < 0 or index >= len(self.valid_manifest):
                raise IndexError(
                    f"Index {index} out of range "
                    f"(0..{len(self.valid_manifest) - 1})"
                )

            row = self.valid_manifest.iloc[index]

            signal_df = pd.read_csv(row["file_path"])

            return signal_df, row["label"]


    def __len__(self):
        if self.valid_manifest is None:
            raise ValueError("Manifest not loaded. Call load_and_align_manifest() first.")
        return len(self.valid_manifest)    
            

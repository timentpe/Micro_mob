from pathlib import Path
from typing import Dict, Tuple

import pandas as pd


def load_dataset(base_path: str = "Dataset_B/Scenario_2") -> Tuple[Dict[str, pd.DataFrame], Dict[str, pd.DataFrame]]:
    """Traverse `base_path` and load all CSV files named `Other_road_users.csv` and `Sensors.csv`.

    Returns two dictionaries:
    - other_road_users: keys formatted as `{transport}_subject_{k}` (for Other_road_users.csv)
    - sensors: keys formatted as `{transport}_subject_{k}` (for Sensors.csv)

    Example:
        other, sensors = load_dataset()
        # keys are lowercase, e.g. 'ebike_subject_a'
        df = other['ebike_subject_a']

    Args:
        base_path: path to `Dataset_B/Scenario_2` (relative or absolute)

    Returns:
        Tuple(two dicts: other_road_users, sensors)
    """
    base = Path(base_path)
    if not base.exists():
        raise FileNotFoundError(f"Base path not found: {base.resolve()}")

    other_road_users: Dict[str, pd.DataFrame] = {}
    sensors: Dict[str, pd.DataFrame] = {}

    for subject_dir in sorted(base.iterdir()):
        if not subject_dir.is_dir():
            continue
        # Expect folders named like Subject_X
        subject_name = subject_dir.name
        if not subject_name.lower().startswith("subject"):
            continue
        # extract subject identifier (last part after underscore if present) and lowercase it
        parts = subject_name.split("_")
        subject_id = parts[-1].lower()

        # for each transport mode in the subject folder
        for transport_dir in sorted(subject_dir.iterdir()):
            if not transport_dir.is_dir():
                continue
            transport = transport_dir.name.lower()

            other_path = transport_dir / "Other_road_users.csv"
            sensors_path = transport_dir / "Sensors.csv"

            if other_path.exists():
                key = f"{transport}_subject_{subject_id}"
                try:
                    other_road_users[key] = pd.read_csv(other_path)
                except Exception as e:
                    raise RuntimeError(f"Error reading {other_path}: {e}")

            if sensors_path.exists():
                key = f"{transport}_subject_{subject_id}"
                try:
                    sensors[key] = pd.read_csv(sensors_path)
                except Exception as e:
                    raise RuntimeError(f"Error reading {sensors_path}: {e}")

    return other_road_users, sensors


def inject_to_namespace(dicts: Dict[str, pd.DataFrame], namespace: dict) -> None:
    """Inject the DataFrames into a namespace (e.g. a notebook `globals()`).

    Usage:
        other, sensors = load_dataset()
        inject_to_namespace(other, globals())

    Warning: this will overwrite any existing variables with the same names.
    """
    for k, v in dicts.items():
        namespace[k] = v

def load_all(base_path: str = "Dataset_B/Scenario_2", inject: bool = False, namespace: dict = None) -> Tuple[Dict[str, pd.DataFrame], Dict[str, pd.DataFrame]]:
    """Load all datasets and optionally inject them into a given namespace.

    Args:
        base_path: path to `Dataset_B/Scenario_2` (relative or absolute)
        inject: if True, inject the loaded DataFrames into the provided namespace
        namespace: the namespace (dict) to inject into if `inject` is True

    Returns:
        Tuple(two dicts: other_road_users, sensors)
    """
    other_road_users, sensors = load_dataset(base_path)
    if inject:
        if namespace is None:
            raise ValueError("Namespace must be provided if inject is True")
        inject_to_namespace(other_road_users, namespace)
        inject_to_namespace(sensors, namespace)
    return other_road_users, sensors
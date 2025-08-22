import pandas as pd
def _strip_cols(df):
    df.columns = [c.strip() if isinstance(c, str) else c for c in df.columns]
    return df

def _dedup_columns(df):
    df = df.loc[:, ~df.columns.duplicated()]
    return df

def _coerce_numeric(df, exclude=("date",)):
    for c in df.columns:
        if c not in exclude:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def _find_date_col_in_multiindex(df):
    for col in df.columns:
        if isinstance(col, tuple):
            if any(isinstance(x, str) and x.strip().lower() == "date" for x in col):
                return col
        elif isinstance(col, str) and col.strip().lower() == "date":
            return col
    return df.columns[0]

def load_2023_2024_station(path, station):
    raw = pd.read_excel(path, header=[0, 1, 2])
    date_col = _find_date_col_in_multiindex(raw)
    ser_date = raw[date_col].squeeze()
    station_df = raw[station].copy()  
    station_df.columns = station_df.columns.get_level_values(0)
    station_df.insert(0, "date", ser_date)
    station_df = _strip_cols(station_df)
    station_df["date"] = pd.to_datetime(station_df["date"], dayfirst=True, errors="coerce")
    station_df = station_df[~station_df["date"].isna()]
    station_df = _dedup_columns(station_df)
    station_df = _coerce_numeric(station_df)
    return station_df

def load_2022_2023_station_only_2022(path, station):
    df = pd.read_excel(path, sheet_name=station)
    df = _strip_cols(df)
    if df.columns[0].strip().lower() != "date":
        df = df.rename(columns={df.columns[0]: "date"})
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")
    df = df[df["date"].dt.year == 2022]
    df = _dedup_columns(df)
    df = _coerce_numeric(df)
    return df

def concat_by_station(file_2223, file_2324, station):
    df22 = load_2022_2023_station_only_2022(file_2223, station)
    df23 = load_2023_2024_station(file_2324, station)

    pollutants = sorted(set(df22.columns).union(df23.columns) - {"date"})
    for c in pollutants:
        if c not in df22.columns:
            df22[c] = pd.NA
        if c not in df23.columns:
            df23[c] = pd.NA

    df22 = df22[["date"] + pollutants]
    df23 = df23[["date"] + pollutants]

    out = pd.concat([df22, df23], ignore_index=True)
    out = out.sort_values("date").reset_index(drop=True)
    return out
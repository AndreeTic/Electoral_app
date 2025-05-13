def process_divipola(path_or_file, candidatos: int):
    import pandas as pd
    import math

    def _normalize_columns(df):
        df.columns = [str(col).strip().replace("\n", " ") for col in df.columns]
        return df

    def _extract_site(header):
        raw = str(header.iloc[0, 0])
        if "_" in raw:
            return raw.split("_")[-2].strip().title()
        return raw.split("\n")[0].strip().title()

    header = pd.read_excel(path_or_file, nrows=1, header=None)
    sitio = _extract_site(header)
    df = pd.read_excel(path_or_file, skiprows=4)
    df = _normalize_columns(df)

    municipal_col = [c for c in df.columns if "comisión municipal" in c.lower()][0]
    general_col   = [c for c in df.columns if "comisión general"  in c.lower()][0]
    aux_cols      = [c for c in df.columns if "comisión auxiliar" in c.lower()]

    municipal = int(df[municipal_col].sum())
    general   = int(df[general_col].sum())
    auxiliar  = int(df[aux_cols[0]].sum()) if aux_cols else 0

    puestos = df[["Puesto", "Mesas"]].dropna()
    puestos["Mesas"] = puestos["Mesas"].astype(int)
    puestos["Remanentes"] = puestos["Mesas"].apply(lambda x: math.ceil(x * 0.10))

    total_mesas    = int(puestos["Mesas"].sum())
    total_rem      = int(puestos["Remanentes"].sum())
    total_mesa_pc  = total_mesas + total_rem
    total_comm_pc  = (municipal + general + auxiliar) * 2

    total_mesa_all = total_mesa_pc * candidatos
    total_comm_all = total_comm_pc * candidatos
    total_all      = total_mesa_all + total_comm_all

    return {
        "sitio": sitio,
        "candidatos": candidatos,
        "puestos": len(puestos),
        "total_mesas": total_mesas,
        "total_remanentes": total_rem,
        "total_mesa_pc": total_mesa_pc,
        "municipal": municipal,
        "general": general,
        "auxiliar": auxiliar * 2,
        "total_comm_pc": total_comm_pc,
        "total_x_candidato": total_mesa_pc + total_comm_pc,
        "total_mesa_all": total_mesa_all,
        "total_comm_all": total_comm_all,
        "total_all": total_all,
    }




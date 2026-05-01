import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")

rename_map = {
    "UserID": "anvandar_id",
    "basket_icon_click": "klickat_varukorgsikon",
    "basket_add_list": "lagt_till_fran_kategorisida",
    "basket_add_detail": "lagt_till_fran_produktsida",
    "sort_by": "anvant_sorteringsfunktion",
    "image_picker": "klickat_pa_produktbild",
    "account_page_click": "gatt_in_pa_kontosida",
    "promo_banner_click": "klickat_pa_kampanjbanner",
    "detail_wishlist_add": "sparat_i_onskelista",
    "list_size_dropdown": "anvant_prissortering",
    "closed_minibasket_click": "stangt_liten_varukorg_popup",
    "checked_delivery_detail": "kollat_fraktkostnad",
    "checked_returns_detail": "kollat_angerratt",
    "sign_in": "loggat_in",
    "saw_checkout": "gatt_till_kassan",
    "saw_sizecharts": "gatt_till_produktspecifikation",
    "saw_delivery": "gatt_till_leveransvillkor",
    "saw_account_upgrade": "tomt_varukorg",
    "saw_homepage": "gatt_till_startsidan",
    "device_mobile": "anvant_mobil",
    "device_computer": "anvant_dator",
    "device_tablet": "anvant_surfplatta",
    "returning_user": "aterkommande_besokare",
    "loc_uk": "besokt_fran_svensk_plats",
    "ordered": "genomfort_bestallning",
}

files = {
    "training_sample.csv": "training_sample_svenska.csv",
    "testing_sample.csv": "testing_sample_svenska.csv",
}

for input_file, output_file in files.items():
    input_path = DATA_DIR / input_file
    output_path = DATA_DIR / output_file

    df = pd.read_csv(input_path)
    df = df.rename(columns=rename_map)
    df.to_csv(output_path, index=False, encoding="utf-8")

    print(f"Created: {output_path}")
    print(df.columns.tolist())
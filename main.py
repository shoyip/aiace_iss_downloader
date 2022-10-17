from dotenv import load_dotenv, find_dotenv
import os
import requests
import tarfile
from pathlib import Path

load_dotenv(find_dotenv())
dest_folder = Path(os.environ.get("DEST_FOLDER"))

# dataset_types = ["iss_80plus",
#     "iss_age_date",
#     "iss_byage",
#     "iss_bydate",
#     "iss_dt",
#     "iss_opsan",
#     "iss_quantili_eta",
#     "iss_ratio_age",
#     "iss_rt",
#     "iss_stack_osp"
# ]

# provinces = ["agrigento", "alessandria", "ancona", "aosta", "arezzo", "ascoli_piceno", "asti", "avellino", "bari", "barletta_andria_trani", "belluno", "benevento", "bergamo", "biella", "bologna", "bolzano", "brescia", "brindisi", "cagliari", "caltanissetta", "campobasso", "caserta", "catania", "catanzaro", "chieti", "como", "cosenza", "cremona", "crotone", "cuneo", "enna", "fermo", "ferrara", "firenze", "foggia", "forli_cesena", "frosinone", "genova", "gorizia", "grosseto", "imperia", "isernia", "laquila", "la_spezia", "latina", "lecce", "lecco", "livorno", "lodi", "lucca", "macerata", "mantova", "massa_carrara", "matera", "messina", "milano", "modena", "monza_brianza", "napoli", "novara", "nuoro", "oristano", "padova", "palermo", "parma", "pavia", "perugia", "pesaro_e_urbino", "pescara", "piacenza", "pisa", "pistoia", "pordenone", "potenza", "prato", "ragusa", "ravenna", "reggio_di_calabria", "reggio_emilia", "rieti", "rimini", "roma", "rovigo", "salerno", "sassari", "savona", "siena", "siracusa", "sondrio", "sud_sardegna", "taranto", "teramo", "terni", "torino", "trapani", "trento", "treviso", "trieste", "udine", "varese", "venezia", "verbano_cusio_ossola", "vercelli", "verona", "vibo_valentia", "vicenza", "viterbo"]

# dataset_name = ["deceduti", "positivi", "ricoveri", "sintomatici", "terapia_intensiva"]

def download(url: str, dest_folder: Path):
    """
    This function downloads the archive in the destination folder.

    Parameters
    ----------
    url: str
        Url of the dataset archive to be downloaded.
    dest_folder: Path
        Path-like object of the destination folder
    """
    # Download the data
    ar_file = dest_folder / "iss_data.tar.gz"
    dest_folder.mkdir(parents=True, exist_ok=True)
    r = requests.get(url)
    with open(ar_file, "wb") as f:
        f.write(r.content)

def unpack(dest_folder: Path):
    """
    This function takes the destination folder as input and unpacks the downloaded
    archive.

    Parameters
    ----------
    dest_folder: Path
        Path-like object of the destination folder
    """
    # Untar the data
    ar_file = dest_folder / "iss_data.tar.gz"
    ar = tarfile.open(ar_file)
    ar.extractall(path = dest_folder / "iss_data")

def main():
    print("Welcome to the ISS Downloader script!")
    print("=====================================\n")

    # Define parameters
    url = "https://covid19.infn.it/iss/csv_part/iss.tar.gz"
    
    print(f"[LOG] Files are going to be downloaded in folder {dest_folder}")

    # Download and unpack the archive
    print("[LOG] Downloading data...")
    download(url, dest_folder)
    print("[LOG] Unpacking data...")
    unpack(dest_folder)
    print("Done!")

if __name__ == "__main__":
    main()

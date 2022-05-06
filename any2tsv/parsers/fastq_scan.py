"""
Example usage: any2tsv fastq-scan fastq-scan.json > fastq-scan.tsv

Example input:
```{bash}
{
    "qc_stats": {
        "total_bp":7500,
        "coverage":0.05,
        "read_total":75,
        "read_min":100,
        "read_mean":100,
        "read_std":0,
        "read_median":100,
        "read_max":100,
        "read_25th":100,
        "read_75th":100,
        "qual_mean":34.0267,
        "qual_std":0.711306,
        "qual_median":34,
        "qual_25th":34,
        "qual_75th":34
    },
    "read_lengths": {

        "100":75
    },
    "per_base_quality": {
        "1":30.7467,        "2":31.5467,        "3":31.5467,        "4":35.44,        "5":34.24,
        "6":34.12,        "7":34.7067,        "8":34.24,        "9":36.9333,        "10":37.0667,
        "11":35.88,        "12":36.0667,        "13":36.72,        "14":38.2667,        "15":37.48,
        "16":38.2133,        "17":36.7467,        "18":37.8267,        "19":36.3333,        "20":37.2933,
        "21":37.9867,        "22":37.1067,        "23":37.4133,        "24":38.2667,        "25":36.6133,
        "26":36.2,        "27":36.3067,        "28":35.8533,        "29":36.5067,        "30":37.72,
        "31":37.3333,        "32":36.0133,        "33":37.4933,        "34":36.1067,        "35":36.76,
        "36":34.8533,        "37":36.3733,        "38":35.1867,        "39":36.0133,        "40":35.3067,
        "41":35.6,        "42":36.7867,        "43":35.52,        "44":37.3333,        "45":36.6533,
        "46":36.8,        "47":35.9867,        "48":35.4533,        "49":35.2,        "50":37.2533,
        "51":35.04,        "52":36,        "53":35.28,        "54":36.16,        "55":35.2,
        "56":33.6133,        "57":36.0533,        "58":34.4533,        "59":35.88,        "60":35.3733,
        "61":35.6933,        "62":34.8267,        "63":35.1067,        "64":35.2933,        "65":32.2667,
        "66":34.4267,        "67":33.9333,        "68":33.6667,        "69":32.6133,        "70":33.4267,
        "71":32.8267,        "72":32.96,        "73":33.5467,        "74":33.1067,        "75":31.8667,
        "76":30.72,        "77":30.6133,        "78":30.2133,        "79":31.7467,        "80":33.8933,
        "81":32.72,        "82":33.1733,        "83":31.5867,        "84":32.6933,        "85":32.0667,
        "86":32.2933,        "87":30.7467,        "88":30.6933,        "89":32.48,        "90":31.08,
        "91":31.6133,        "92":31.72,        "93":30.3867,        "94":30.7067,        "95":29.9733,
        "96":31.96,        "97":32.44,        "98":30.2267,        "99":31.2533,        "100":30.2267
    }
}
```

Example output (transposed with csvtk for readability):
```{bash}
any2tsv fastq-scan fastq-scan.json | csvtk transpose -t
filename        fastq-scan.json
total_bp        7500
coverage        0.05
read_total      75
read_min        100
read_mean       100
read_std        0
read_median     100
read_max        100
read_25th       100
read_75th       100
qual_mean       34.0267
qual_std        0.711306
qual_median     34
qual_25th       34
qual_75th       34
```
"""
import json
from os.path import basename
__name__ = "fastq-scan"
__description__ = "Generate FASTQ summary statistics in JSON format"

def parse(input_file: str) -> dict:
    """
    A function to parse a JSON file generated by [fastq-scan](https://github.com/rpetit3/fastq-scan)

    Args:

    `input_file`: A filepath to the `fastq-scan` output file.

    Returns:

    A dictionary containing the values from only the `qc_stats` list in the JSON file.
    """
    with open(input_file, 'rt') as f:
        data = json.load(f)
    return {'filename': basename(input_file), **data['qc_stats']}

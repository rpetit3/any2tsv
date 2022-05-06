*__Note: This repo is under active development. So it'll be changing a lot__*

# any2tsv
Convert various bioinformatic outputs to TSV

## Motivation
Well you see I have this pipeline called [Bactopia](https://bactopia.github.io/) for the analysis of bacterial genomes, and
it [produces a lot of output files](https://bactopia.github.io/output-overview/). I started making parsers for these outputs,
but I didn't want them to be hidden in Bactopia. Instead, I wanted create a simple tool (e.g. Torsten Seemann's [`any2fasta`](https://github.com/tseemann/any2fasta))
the community could use.

Although, please keep in mind, unless there are outside contributions, the available parsers will be reflective of tools
I use in Bactopia. I frankly don't have the bandwidth to expand further. But, please don't worry, if you would like to
add a parser for a tool that you use, by all means lets get it added!

## Installation
I'm too early in the game for this, but you can expect it to be available from pip and Bioconda in due time.

## Usage

```{bash}
any2tsv --help

 Usage: any2tsv [OPTIONS] <tool name> <input file>

╭─ Options ────────────────────────────────────────────────────────────────────────────────────────╮
│  --version           Show the version and exit.                                                  │
│  --list_tools        List tools with an available parser.                                        │
│  --help        -h    Show this message and exit.                                                 │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯

```

## Example Usage
### `fastq-scan`
Let's start with [`fastq-scan`](https://github.com/rpetit3/fastq-scan), which is a simple tool to output FASTQ summary
statistics in JSON format. Because its already in JSON format, this is an easy conversion to TSV.

#### Example `fastq-scan` Output
```{bash}
cat fastq-scan.json
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

#### Converting `fastq-scan` to TSV
```{bash}
any2tsv fastq-scan fastq-scan.json
filename        total_bp        coverage        read_total      read_min        read_mean       read_std        read_median     read_max        read_25th       read_75th       qual_mean       qual_std        qual_median     qual_25th       qual_75th
fastq-scan.json 7500    0.05    75      100     100     0       100     100     100     100     34.0267 0.711306        34      34      34
```

You might be wondering, *Where'd the read lengths and per-base qualities go?*. Well, honestly, I didn't think they were
use in TSV format, so out they went. But, if for some reason you think they would be useful, please let me know.

# Naming
I think its pretty obvious, but the name `any2tsv` is inspired by Torsten Seemann's [`any2fasta`](https://github.com/tseemann/any2fasta). `any2fasta`
converts many different formats to FASTA format. I wanted to do the same except TSV outputs. These TSV outputs can then be easily manipulated by
the user.

## Author

* Robert A. Petit III
* Web: [https://www.robertpetit.com](https://www.robertpetit.com)
* Twitter: [@rpetit3](https://twitter.com/rpetit3)

# VaslApp v5 generator
This repository provided for vasl baas team to generate initial stuff for a new entity,
including entity class, repository, service, adapter and so on.

## Installation
`pip install vaslapp5generator`

## Configuration
Provide a config file where you want to use the command.  
Use **config.example.py** to provide **config.py** configuration file.  

## Usage

### Config file
Run the command to generate a sample config file named **va-config.json**.

```vaslapp5generator config```

Then you need to edit this file according to your needs. 

### Generate files for an entity

After generating and editing config file, run this command to generate entity.

```vaslapp5generator entity```

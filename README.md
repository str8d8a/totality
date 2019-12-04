# Totality

> The peculiar character of the problem of a rational economic order is determined precisely by the fact that the knowledge of the circumstances of which we must make use never exists in concentrated or integrated form...it is a problem of the utilization of knowledge which is not given to anyone in its totality.

--Hayek, "The Use of Knowledge in Society"

Challenge accepted.

## Goals

This repository contains schemas that collectively document entities that underlie the global economy of all goods, as well as the energy system that underlies it.

The goals of this schema are as follows:

1. To describe the physical underpinnings and events that comprise the functioning of the primary and secondary economic sectors.
2. To provide a clear, open, accessible format by which a widely-distributed group of otherwise unaffiliated contributors can collect and submit observations of economic activity.
3. To support inferences and enrichment activities that build on publicly-available observations.

## Principles

1. Use existing metadata and coding schemes wherever possible
2. Represent those details that are needed either to accurately capture the content of economic activity, or to approriately track the facilities and infrastructure that is used to perform those activities
3. Accept, whenever possible, incomplete or uncertain observations

## Concepts and Entities

### Reservoir

[Schema](/str8d8a/totality/blob/master/schemas/reservoir.schema.json)

All containers that hold an economically valuable material or materials at any stage in a supply chain, from raw material to finished product ready for distribution and sale. Note that the materials in question include both matter, at all stages of processing and refinement, and energy in any useful and recoverable form.

### Facility

[Schema](/str8d8a/totality/blob/master/schemas/facility.schema.json)

### Conveyance

[Schema](/str8d8a/totality/blob/master/schemas/conveyance.schema.json)

All specific and individual means by which goods are transported from one location to another. This includes the well-known multimodal container transport system, bulk shipment of commodities, pipelines, and electricity transmission and distribution lines.

### Observation

[Schema](/str8d8a/totality/blob/master/schemas/observation.schema.json)

A core tenet of this publishing standard is the idea that the information submitted is not factual, but rather of uncertain status. Data submitted is therefore always enclosed in an observation, which includes information about the source and means of collection. This standard does not prescribe the principles or methods by which these uncertainties should be resolved, nor how potentially conflicting observations should be reconciled.

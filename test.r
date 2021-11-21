#setRepositories(ind = 1:2)
#if (!requireNamespace("BiocManager", quietly = TRUE))
 #   install.packages("BiocManager")

#BiocManager::install("GenomeInfoDb")

#BiocManager::install("HSMMSingleCell")
#install.packages("devtools")
#devtools::install_github('cole-trapnell-lab/leidenbase')
#devtools::install_github('cole-trapnell-lab/monocle3')
#install.packages('Seurat',Ncpus=6,dependencies=TRUE)

library(Seurat)
library(SeuratData)
if (!requireNamespace("remotes", quietly = TRUE)) {
  install.packages("remotes")
}
remotes::install_github("mojaveazure/seurat-disk")
library(SeuratDisk)
Convert("pbmc_multimodal.h5Seurat",dest="h5ad")

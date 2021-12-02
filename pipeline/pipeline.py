import anndata
import scanpy as sc
import sfaira
sc.logging.print_version_and_date()
sc.settings.verbosity = 0
sc.set_figure_params()


def ui_adata(adata, model_name) -> 'adata':
   ui = sfaira.ui.UserInterface(sfaira_repo=True)
   ui.zoo_celltype.model_id = model_name
   ui.load_data(adata, gene_symbol_col='index')
   ui.load_model_celltype()
   ui.predict_celltype()
   if "X_umap" not in ui.data.adata.obsm.keys():
      sc.pp.normalize_total(ui.data.adata)
      sc.pp.log1p(ui.data.adata)
      sc.pp.pca(ui.data.adata)
      sc.pp.neighbors(ui.data.adata)
      sc.tl.umap(ui.data.adata)
   return ui.data.adata


def ui(x: str) -> 'Dict':
   """
   :param x: is path to object
   :returns: dictionary of UMAP and cell type labels
   """
   # TODO add switch over different data representations form reading functions here: https://scanpy.readthedocs.io/en/stable/api.html#reading
   model_name = 'celltype_human-blood-mlp-0.1.3-0.1_theislab'  # hard coded model name
   adata = ui_adata(x, model_name=model_name)
   return {"umap": adata.obsm["X_umap"], "cell_type": adata.obs.loc[:, "celltype"]}


result = ui(anndata.read_h5ad('./pbmc_multimodal.h5ad'))

print(result)
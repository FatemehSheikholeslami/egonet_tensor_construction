# egonet_tensor_construction
This script makes a text file corresponding to the sparse "egonet tensor representation" of a network given by its edgelist.




 DC_Egoten.py [-h] [--input [INPUT]] [--output [OUTPUT]]
                    [--workers WORKERS] [--directed] [--undirected]                 
                    [--ordered] [--unordered]



	--input                 (dataset_adj.txt) is the edgeset dataset with a pair of nodes in each line separated by comma ',' (default facebook_adj.txt)
	--output                the output sparse tensor corresponding to the sparse egonet tensor.(default=egonet_tensor.txt)
	--directed		use if edgelist is directed
	--undirected 		use if edgelist is undirected (default)
	--ordered		use if node indexing in the edgelist starts from 1 and there is no gap in node ids. (default)
	--unordered		use if node ids in the edgelist do not start form 1, or if there is a gap in indexing. 
	--workers		number of workers (set 1 as default)
        
     
If the node indexing in the edgelist is not ordered, e.g. there is gap between node indices, use "--unordered" so that the nodes are first ordered, and then the egonet tensor is constructed using the ordered indices.
'ordered_edgelist' and 'node_mapping.txt' are also produced in this case for reference.

For instance, to execute, run:
	python  build_egoten.py --input facebook_adj.edges --undirected --workers 4 --ordered

%%%% OUTPUT FILES
The output file is "egonet_tensor.txt" where each line is the the index of non-zero entries followed by its value (1 as default as in binary networks).

Additionally, if "unordered" is set, then the file "node_mapping.txt" will be produced where each line gives the mapping from the "original" to the "ordered" id of nodes.   



******************************************************************************************
For more information, please see:
F. Sheikholeslami and G. B. Giannakis, "Overlapping community detection via constrained parafac: a divide and conquer approach," ICDM, New Orleans, LA, Nov. 2017.

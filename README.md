# egonet_tensor_construction
This script makes a text file corresponding to the sparse tensor representation of a network given by its edgelist.




 DC_Egoten.py [-h] [--input [INPUT]] [--output [OUTPUT]]
                    [--workers WORKERS] [--directed] [--undirected]                 
                    [--ordered] [--unordered]



	--input                 (dataset_adj.txt) is the edgeset dataset with a pair of nodes in each line separated by comma ',' (default fixed_facebook_adj.txt)
	--output                is the output file where each lien is the node s assigned to a detected community (default )
	--top_K                 is the K community number for the top EgoTen application (default 100)
	--lower_K		is the K community number for the consequtive EgoTen application (default 2)
	--max_depth		is the maximum allowed depth for the tree (conscutive application of EgoTen) (default 10)
	--directed		use  if edgelist is directed
	--undirected 		use of edgelist is undirected
	--C_max			is the desired (maximum size) resolution of a community (set to 10% of the graph size)
	--workers		number of workers (set 1 as default)
        
     


For instance, to execute, run:
	python  build_egoten.py --input facebook_adj.edges --undirected --workers 4 --ordered

%%%% OUTPUT FILES
The output file is "egonet_tensor.txt" where each line is the 
If "unordered" is set, then the file "node_mapping.txt" will be produced where each line gives the "original" and "ordered" id of nodes.   




For more information, please see:
F. Sheikholeslami and G. B. Giannakis, "Overlapping community detection via constrained parafac: a divide and conquer approach," ICDM, New Orleans, LA, Nov. 2017.

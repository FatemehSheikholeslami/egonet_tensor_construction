#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 17:43:35 2018

@author: fateme sheikholeslami
"""
try:
    import numpy as np
    import scipy as sp
    import networkx as nx
    import commands
    import egoten_utility as GEN
    import argparse
    from operator import itemgetter
    import main_fix
    
except ImportError as e:
    print "Application depends on numpy, scipy, matplotlib, networkx"
    print "Stack trace:"
    print e.strerror



def make_egoten(input_adj,directed_flag,nworker,ordered,outputfile):  

  if not ordered: 
    print 'asdasd'
    dict_map = main_fix.fix_adj(input_adj)
    input_adj = 'ordered_'+input_adj  
  ###################    Form networkx graph    #########################  
  if directed_flag:  
    G=GEN.edgelist2networkxG_directed(input_adj)
  else:   
    G=GEN.edgelist2networkxG_undirected(input_adj)

  if directed_flag:
    map_here=GEN.make_ego_tensor_directed(G,outputfile,nworker)
  else:
    map_here=GEN.make_ego_tensor_undirected(G,outputfile,nworker)  
  return





def parse_args():
  
    parser = argparse.ArgumentParser(description="Run tensor_decomp")
    parser.add_argument('--input', nargs='?', default= 'facebook_adj.edges', 
	                    help='Input edgelist file, separated by space, default = facebook_adj.edges')
    parser.add_argument('--output', nargs='?', default= 'egonet_tensor.txt', 
	                    help='Output file name, default  = communities.txt')	
    parser.add_argument('--workers', type=int, default=8,
	                    help='Number of parallel workers for tensor construction. Default is 8.')
 
    parser.add_argument('--directed', dest='directed', action='store_true',
	                    help='Graph is (un)directed. Default is undirected.')
    parser.add_argument('--undirected', dest='directed', action='store_false')
    parser.set_defaults(directed=False)
    parser.add_argument('--ordered', dest='ordered' ,action = 'store_true',
	                    help='set if nodes in the edgelist are ordered (no gap in numbering).')
    parser.add_argument('--unordered', dest='ordered' ,action = 'store_false',
	                    help='set if ordering of nodes in the edgelist is required. ORIGINAL ORDERING OF NODES WILL BE LOST.')
    parser.set_defaults(ordered='Error')
    return parser.parse_args()




if __name__=='__main__':

  args = parse_args()
  print '************ Running DC_Egoten ****************'
  print 'Edgelist input ' + args.input
  print 'Output file ' + args.output
  print '# of workers for tensor construction : ' + str(args.workers)
  if args.directed:
    print 'Network type: Directed'
  else:
    print 'Network type: Undirected'
  if args.ordered:
    print 'Node-numbering status : ordered'
  else:
    print 'Node-numbering status: unordered'
  if args.ordered=='Error':
    print '****Usage error: Must set whether the edgelist is ordered or not (if there is gap in oroginal node numbering). See help.****'
  else:
    make_egoten(args.input, args.directed , args.workers,args.ordered,args.output)
  # make_egoten(input_adj,directed_flag,nworker,ordered,output):  





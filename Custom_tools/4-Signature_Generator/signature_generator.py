import sys
sys.path.append('../polygraph')
import cPickle
import polygraph.sig_gen.lcseq_tree
import time

def convert_snort_signature(generated_polygraph_signature):
	regexed_signature = '/'
	for signature_component in generated_polygraph_signature.tuplesig:
		regexed_signature += str(signature_component).encode('string-escape')+ '(.|\\s)*'
	#delete trailing dot star (.|\s*)
	regexed_signature = regexed_signature [:-7]
	regexed_signature += '/'

	snort_signature = 'reject tcp any any -> any 80 (pcre:"%s"; sid:1000001;)' % regexed_signature
	return snort_signature

if __name__ == '__main__':

	#limit sample because algorithm o(n^2)
	limit = 100

	#load worm workloads
	f = open("worm.pickle")
	worms = cPickle.load(f)[:limit]
	f.close()

	#load innocuous pool
	training_streams = "/home/minta/Documents/traces/training.80.streams"

	#load signature generator
	stats = None #not using statistic knowledge
	signature_generator = polygraph.sig_gen.lcseq_tree.LCSeqTree(pname="Token Subsequence", fname="lcseq", kfrac=1, tokenize_all=True, tokenize_pairs=False, minlen=2,statsfile=stats, do_cluster=False) #non clustered
	#signature_generator = polygraph.sig_gen.lcseq_tree.LCSeqTree(pname="Token Subsequence", fname="lcseq_tree", k=3, tokenize_all=True, tokenize_pairs=False, minlen=2,statsfile=stats, spec_threshold=3, max_fp_count=5, fpos_training_streams=training_streams, min_cluster_size=3)#clustered

	#generate signature and print to file
	t0 = time.time()
	generated_signatures = signature_generator.train(worms)
	t1 = time.time()
	deltat = t1-t0

	f = open("generated_signature.txt",'w')
	for generated_signature in generated_signatures:
		f.write(convert_snort_signature(generated_signature))
		print convert_snort_signature(generated_signature)	
	f.close()
	print '\n'
	print 'elapsed time = %f s' % deltat

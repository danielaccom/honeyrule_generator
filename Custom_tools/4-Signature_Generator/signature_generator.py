import sys
sys.path.append('../polygraph')
import cPickle
import polygraph.sig_gen.lcseq_tree

def convert_snort_signature(generated_polygraph_signature):
	regexed_signature = '/'
	for signature_component in generated_polygraph_signature.tuplesig:
		regexed_signature += str(signature_component).encode('string-escape')+ '.*'
	#delete trailing dot star (.*)
	regexed_signature = regexed_signature [:-2]
	regexed_signature += '/'

	snort_signature = 'reject tcp any any -> any 80 (pcre:"%s"; sid:1000001; msg:"generated 1000001 rule";)' % regexed_signature
	return snort_signature

if __name__ == '__main__':

	#load worm workloads
	f = open("apache.pickle")
	worms = cPickle.load(f)[:8]
	f.close()

	#load innocuous pool
	training_streams = "/home/minta/Documents/traces/training.80.streams"

	#load signature generator
	stats = None #not using statistic knowledge
	signature_generator = polygraph.sig_gen.lcseq_tree.LCSeqTree(pname="Token Subsequence", fname="lcseq", kfrac=1, tokenize_all=True, tokenize_pairs=False, minlen=2,statsfile=stats, do_cluster=False) #non clustered
	#signature_generator = polygraph.sig_gen.lcseq_tree.LCSeqTree(pname="Token Subsequence", fname="lcseq_tree", k=3, tokenize_all=True, tokenize_pairs=False, minlen=2,statsfile=stats, spec_threshold=3, max_fp_count=5, fpos_training_streams=training_streams, min_cluster_size=3)#clustered

	#generate signature and print to file
	generated_signatures = signature_generator.train(worms)

	f = open("generated_signature.txt",'w')
	for generated_signature in generated_signatures:
		f.write(convert_snort_signature(generated_signature))
		print convert_snort_signature(generated_signature)	
	f.close()
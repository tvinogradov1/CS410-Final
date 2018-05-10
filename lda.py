import sys
import metapy

# get values from command line
config = sys.argv[1] # config.toml
output_prefix = sys.argv[2] # output
num_topics = list(map(int, [sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8]])) # topics list

# loop through each topic number
for num_topic in num_topics:

    metapy.log_to_stderr()
    fidx = metapy.index.make_forward_index(config)
    dset = metapy.learn.Dataset(fidx)
    lda_inf = metapy.topics.LDAGibbs(dset, num_topics=num_topic, alpha=0.1, beta=0.1)
    lda_inf.run(num_iters=1000)
    lda_inf.save(output_prefix)

    model = metapy.topics.TopicModel(output_prefix)

    # add topic distributions from document
    output_topics_file = open("outputs/" + str(num_topic) + "_topics.txt",'w+')
    with output_topics_file as topic:
        for topic_id in range(num_topic):
            topic.write('Topic ' + str(topic_id) + '\n')
            topic.write(str([(fidx.term_text(pr[0]), pr[1]) for pr in model.top_k(tid=topic_id, k = 20)]))
            topic.write('\n')

    target_doc_count = 5
    # add topic proportions from document
    output_doc_file = open("outputs/" + str(num_topic) + "_topics.txt",'a')
    with output_doc_file as doc:
        doc.write('\n\n')
        for d_id in range(target_doc_count):
            doc.write('Document ' + str(d_id) + '\n')
            doc.write(str(model.topic_distribution(d_id)))
            doc.write('\n')

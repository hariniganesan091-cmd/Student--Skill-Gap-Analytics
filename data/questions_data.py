# 255 Assessment Questions across 7 Career Roles and 51 Skill Categories
# Every skill in every career role contains EXACTLY 5 questions.
# Q1 = Basic, Q2 = Beginner, Q3 = Intermediate, Q4 = Advanced, Q5 = Expert

QUESTIONS_DATA = {   'AI/ML Engineer': {   'Big Data': [   {   'answer': 'HDFS',
                                              'difficulty': 'Basic',
                                              'options': ['HDFS', 'S3', 'NFS', 'GFS'],
                                              'q': 'What distributed file system stores big data across commodity '
                                                   'hardware clusters in Apache Hadoop?'},
                                          {   'answer': 'Apache Spark',
                                              'difficulty': 'Beginner',
                                              'options': [   'Apache Spark',
                                                             'Apache Hadoop MapReduce',
                                                             'Apache Hive',
                                                             'Apache Pig'],
                                              'q': 'Which distributed compute engine processes data in-memory for fast '
                                                   'big data processing?'},
                                          {   'answer': 'RDD (Resilient Distributed Dataset)',
                                              'difficulty': 'Intermediate',
                                              'options': [   'RDD (Resilient Distributed Dataset)',
                                                             'DataFrame',
                                                             'DataStream',
                                                             'Dataset'],
                                              'q': 'What fundamental abstraction in Apache Spark represents an '
                                                   'immutable distributed collection of elements?'},
                                          {   'answer': 'Uneven distribution of key values causes single partition '
                                                        'executor tasks to bottleneck; resolved by salting keys or '
                                                        'map-side aggregation',
                                              'difficulty': 'Advanced',
                                              'options': [   'Uneven distribution of key values causes single '
                                                             'partition executor tasks to bottleneck; resolved by '
                                                             'salting keys or map-side aggregation',
                                                             'Insufficient CPU cores on master node; resolved by '
                                                             'adding master nodes',
                                                             'Garbage collection overhead; resolved by converting '
                                                             'DataFrames to RDDs',
                                                             'File format incompatibility; resolved by saving as CSV'],
                                              'q': 'What causes Data Skew during Spark shuffle transformations (e.g. '
                                                   '`groupByKey`), and how can it be resolved?'},
                                          {   'answer': 'Apache Kafka for event streaming + Spark Structured Streaming '
                                                        'for windowed processing + Redis / Cassandra for low-latency '
                                                        'feature serving',
                                              'difficulty': 'Expert',
                                              'options': [   'Apache Kafka for event streaming + Spark Structured '
                                                             'Streaming for windowed processing + Redis / Cassandra '
                                                             'for low-latency feature serving',
                                                             'Hadoop MapReduce jobs writing to HDFS flat files every '
                                                             '24 hours',
                                                             'Python script reading raw JSON logs directly over SFTP',
                                                             'Single SQLite database instance on worker node'],
                                              'q': 'When architecting a real-time feature store pipeline processing '
                                                   'millions of event streams, what technology stack handles event '
                                                   'streaming and feature lookup?'}],
                          'C': [   {   'answer': 'malloc()',
                                       'difficulty': 'Basic',
                                       'options': ['malloc()', 'alloc()', 'new()', 'create()'],
                                       'q': 'Which standard library function dynamically allocates memory on the heap '
                                            'in C?'},
                                   {   'answer': '*',
                                       'difficulty': 'Beginner',
                                       'options': ['*', '&', '->', '.'],
                                       'q': 'What operator is used to dereference a pointer in C?'},
                                   {   'answer': 'free(ptr)',
                                       'difficulty': 'Intermediate',
                                       'options': ['free(ptr)', 'delete(ptr)', 'dealloc(ptr)', 'clear(ptr)'],
                                       'q': 'How do you free dynamically allocated memory in C to prevent memory '
                                            'leaks?'},
                                   {   'answer': 'Buffer Overflow',
                                       'difficulty': 'Advanced',
                                       'options': [   'Buffer Overflow',
                                                      'Null Pointer Dereference',
                                                      'Use-After-Free',
                                                      'Format String Bug'],
                                       'q': 'What security vulnerability occurs when writing data past the allocated '
                                            'length of a buffer in C?'},
                                   {   'answer': 'By aligning thread-specific variables on separate cache line '
                                                 'boundaries (e.g., 64 bytes) to avoid invalidating CPU L1/L2 caches',
                                       'difficulty': 'Expert',
                                       'options': [   'By aligning thread-specific variables on separate cache line '
                                                      'boundaries (e.g., 64 bytes) to avoid invalidating CPU L1/L2 '
                                                      'caches',
                                                      'By disabling CPU hardware caches entirely',
                                                      'By storing all struct attributes as void pointers',
                                                      'By converting C structs to packed bitfields'],
                                       'q': 'In high-performance embedded AI runtimes, how does Cache Line Padding in '
                                            "C structures prevent 'False Sharing' on multi-core CPUs?"}],
                          'C++': [   {   'answer': 'Destructors',
                                         'difficulty': 'Basic',
                                         'options': [   'Destructors',
                                                        'Constructors',
                                                        'Smart Pointers',
                                                        'Garbage Collector'],
                                         'q': 'Which feature in C++ allows automatic memory cleanup when an object '
                                              'goes out of scope?'},
                                     {   'answer': 'std::vector',
                                         'difficulty': 'Beginner',
                                         'options': ['std::vector', 'std::list', 'std::array', 'std::set'],
                                         'q': 'Which C++ Standard Template Library (STL) container represents a '
                                              'dynamic array that automatically resizes?'},
                                     {   'answer': 'std::unique_ptr',
                                         'difficulty': 'Intermediate',
                                         'options': [   'std::unique_ptr',
                                                        'std::shared_ptr',
                                                        'std::weak_ptr',
                                                        'std::auto_ptr'],
                                         'q': 'Which modern C++ smart pointer enforces exclusive single ownership of a '
                                              'dynamically allocated resource?'},
                                     {   'answer': 'Move Semantics and Rvalue References (`&&`)',
                                         'difficulty': 'Advanced',
                                         'options': [   'Move Semantics and Rvalue References (`&&`)',
                                                        'Virtual Function Overriding',
                                                        'Template Specialization',
                                                        'Friend Classes'],
                                         'q': 'What feature introduced in C++11 enables moving resources from '
                                              'temporary objects without deep copying?'},
                                     {   'answer': 'Using SIMD intrinsics (AVX-512 / NEON) combined with explicit '
                                                   'memory alignment (`alignas`) and loop unrolling',
                                         'difficulty': 'Expert',
                                         'options': [   'Using SIMD intrinsics (AVX-512 / NEON) combined with explicit '
                                                        'memory alignment (`alignas`) and loop unrolling',
                                                        'Replacing pointer arithmetic with recursive virtual method '
                                                        'calls',
                                                        'Allocating all matrices on heap using `malloc()` inside loops',
                                                        'Wrapping C++ loops inside Python string execution calls'],
                                         'q': 'When optimizing tensor computation kernels in C++ for machine learning '
                                              'inference, what low-level technique maximizes SIMD hardware '
                                              'utilization?'}],
                          'Deep Learning': [   {   'answer': 'ReLU',
                                                   'difficulty': 'Basic',
                                                   'options': ['ReLU', 'Sigmoid', 'Tanh', 'Softmax'],
                                                   'q': 'What non-linear activation function computes `f(x) = max(0, '
                                                        'x)` in neural networks?'},
                                               {   'answer': 'Convolutional Neural Network (CNN)',
                                                   'difficulty': 'Beginner',
                                                   'options': [   'Convolutional Neural Network (CNN)',
                                                                  'Recurrent Neural Network (RNN)',
                                                                  'Multi-Layer Perceptron (MLP)',
                                                                  'Autoencoder'],
                                                   'q': 'Which neural network architecture is tailored for grid-like '
                                                        'spatial data like images?'},
                                               {   'answer': 'Backpropagation',
                                                   'difficulty': 'Intermediate',
                                                   'options': [   'Backpropagation',
                                                                  'Forward Pass',
                                                                  'Gradient Ascent',
                                                                  'Convolution'],
                                                   'q': 'What algorithm computes loss gradients with respect to neural '
                                                        'network weights using the chain rule?'},
                                               {   'answer': 'Self-Attention Mechanism (Scaled Dot-Product Attention)',
                                                   'difficulty': 'Advanced',
                                                   'options': [   'Self-Attention Mechanism (Scaled Dot-Product '
                                                                  'Attention)',
                                                                  'Recurrent Gated Hidden Units',
                                                                  'Max Pooling Layers',
                                                                  'Batch Normalization'],
                                                   'q': 'What mechanism in Transformer models (e.g., BERT, GPT) '
                                                        'enables modeling relationships between words regardless of '
                                                        'positional distance?'},
                                               {   'answer': 'Gradients exponentially shrink/explode during backprop '
                                                             'across deep layers; Residual skip connections create '
                                                             'identity paths allowing gradients to flow directly',
                                                   'difficulty': 'Expert',
                                                   'options': [   'Gradients exponentially shrink/explode during '
                                                                  'backprop across deep layers; Residual skip '
                                                                  'connections create identity paths allowing '
                                                                  'gradients to flow directly',
                                                                  'Vanishing gradients happen when learning rate is '
                                                                  'too high; skip connections double learning rate',
                                                                  'Exploding gradients crash GPU memory; skip '
                                                                  'connections offload activations to CPU',
                                                                  'Skip connections replace matrix multiplications '
                                                                  'with addition'],
                                                   'q': 'When training deep neural networks (100+ layers), how do '
                                                        'Vanishing/Exploding Gradients occur and how do Residual '
                                                        'Connections (ResNets) mitigate them?'}],
                          'Java': [   {   'answer': 'extends',
                                          'difficulty': 'Basic',
                                          'options': ['extends', 'implements', 'inherits', 'super'],
                                          'q': 'Which keyword is used to inherit a class in Java?'},
                                      {   'answer': 'Heap Memory',
                                          'difficulty': 'Beginner',
                                          'options': [   'Heap Memory',
                                                         'Stack Memory',
                                                         'Metaspace',
                                                         'Program Counter Register'],
                                          'q': 'Which memory area in JVM stores Java object instances?'},
                                      {   'answer': 'Stream API',
                                          'difficulty': 'Intermediate',
                                          'options': ['Stream API', 'Reflection API', 'Generics', 'Serialization'],
                                          'q': 'Which Java 8 feature allows functional style processing of sequences '
                                               'of elements?'},
                                      {   'answer': 'By tracing object reference graphs starting from Garbage '
                                                    'Collection (GC) Roots',
                                          'difficulty': 'Advanced',
                                          'options': [   'By tracing object reference graphs starting from Garbage '
                                                         'Collection (GC) Roots',
                                                         'By keeping a reference counter on each object',
                                                         'By checking if objects are older than 10 seconds',
                                                         'By scanning disk storage logs'],
                                          'q': 'How does the Java Garbage Collector (GC) identify unreachable objects '
                                               'eligible for collection?'},
                                      {   'answer': 'Use low-latency garbage collectors like ZGC / Shenandoah and '
                                                    'reuse object pools for request tensors',
                                          'difficulty': 'Expert',
                                          'options': [   'Use low-latency garbage collectors like ZGC / Shenandoah and '
                                                         'reuse object pools for request tensors',
                                                         'Increase thread stack size to 1GB',
                                                         'Disable JVM Bytecode verification',
                                                         'Call `System.gc()` inside every HTTP controller handle '
                                                         'method'],
                                          'q': 'In high-throughput enterprise ML model scoring services in Java, how '
                                               'do you mitigate Garbage Collection latency spikes (Stop-The-World '
                                               'pauses)?'}],
                          'Linear Algebra': [   {   'answer': 'N x P matrix',
                                                    'difficulty': 'Basic',
                                                    'options': [   'N x P matrix',
                                                                   'M x M matrix',
                                                                   'N x N matrix',
                                                                   'P x N matrix'],
                                                    'q': 'What is the result of multiplying an N x M matrix by an M x '
                                                         'P matrix?'},
                                                {   'answer': 'Eigenvector',
                                                    'difficulty': 'Beginner',
                                                    'options': [   'Eigenvector',
                                                                   'Unit vector',
                                                                   'Orthogonal vector',
                                                                   'Gradient vector'],
                                                    'q': 'What vector satisfies the equation `A * v = lambda * v` for '
                                                         'a square matrix A?'},
                                                {   'answer': 'Singular Value Decomposition (SVD)',
                                                    'difficulty': 'Intermediate',
                                                    'options': [   'Singular Value Decomposition (SVD)',
                                                                   'LU Decomposition',
                                                                   'Cholesky Decomposition',
                                                                   'QR Decomposition'],
                                                    'q': 'What matrix factorization technique decomposes any M x N '
                                                         'real matrix into `U * Sigma * V^T`?'},
                                                {   'answer': 'Eigenvectors specify orthogonal directions of maximum '
                                                              'variance, and corresponding Eigenvalues quantify '
                                                              'variance magnitude along those axes',
                                                    'difficulty': 'Advanced',
                                                    'options': [   'Eigenvectors specify orthogonal directions of '
                                                                   'maximum variance, and corresponding Eigenvalues '
                                                                   'quantify variance magnitude along those axes',
                                                                   'Eigenvectors invert matrix values to eliminate '
                                                                   'negative numbers',
                                                                   'Eigenvectors convert dense matrices into sparse '
                                                                   'diagonal matrices',
                                                                   'Eigenvectors project non-linear data into infinite '
                                                                   'dimensional space'],
                                                    'q': 'How does Principal Component Analysis (PCA) utilize '
                                                         'Eigenvectors of the covariance matrix for dimensionality '
                                                         'reduction?'},
                                                {   'answer': 'High condition number means small perturbations in '
                                                              'input b cause massive errors in solution x, causing '
                                                              'severe gradient instability during optimization',
                                                    'difficulty': 'Expert',
                                                    'options': [   'High condition number means small perturbations in '
                                                                   'input b cause massive errors in solution x, '
                                                                   'causing severe gradient instability during '
                                                                   'optimization',
                                                                   'Low condition number causes matrix multiplication '
                                                                   'to throw division-by-zero errors',
                                                                   'Ill-conditioned matrices cannot be transposed',
                                                                   'Condition number measures the total RAM occupied '
                                                                   'by matrix entries'],
                                                    'q': 'Why is the condition number of a matrix crucial in solving '
                                                         'linear systems `A * x = b`, and how does an ill-conditioned '
                                                         'matrix affect ML model optimization?'}],
                          'Machine Learning': [   {   'answer': 'Supervised Learning',
                                                      'difficulty': 'Basic',
                                                      'options': [   'Supervised Learning',
                                                                     'Unsupervised Learning',
                                                                     'Reinforcement Learning',
                                                                     'Self-Supervised Learning'],
                                                      'q': 'Which machine learning paradigm uses labeled training data '
                                                           'to predict outcomes?'},
                                                  {   'answer': 'Overfitting',
                                                      'difficulty': 'Beginner',
                                                      'options': [   'Overfitting',
                                                                     'Underfitting',
                                                                     'High Bias',
                                                                     'Data Leakage'],
                                                      'q': 'What problem occurs when a model performs exceptionally '
                                                           'well on training data but poorly on unseen test data?'},
                                                  {   'answer': 'F1-Score',
                                                      'difficulty': 'Intermediate',
                                                      'options': [   'F1-Score',
                                                                     'Accuracy',
                                                                     'Mean Squared Error (MSE)',
                                                                     'R-Squared'],
                                                      'q': 'Which metric evaluates classification model performance by '
                                                           'harmonic mean of Precision and Recall?'},
                                                  {   'answer': 'It builds decision trees sequentially, where each new '
                                                                'tree fits on the residual errors (pseudo-residuals) '
                                                                'of the previous models',
                                                      'difficulty': 'Advanced',
                                                      'options': [   'It builds decision trees sequentially, where '
                                                                     'each new tree fits on the residual errors '
                                                                     '(pseudo-residuals) of the previous models',
                                                                     'It builds independent trees in parallel and '
                                                                     'averages their predictions',
                                                                     'It randomly drops tree nodes during evaluation',
                                                                     'It calculates linear weights using matrix '
                                                                     'inversion'],
                                                      'q': 'How does Gradient Boosting (e.g., XGBoost) build ensemble '
                                                           'decision trees?'},
                                                  {   'answer': 'L1 adds absolute weight penalty forcing coefficients '
                                                                'to zero (feature selection); L2 adds squared weight '
                                                                'penalty shrinking weights towards zero',
                                                      'difficulty': 'Expert',
                                                      'options': [   'L1 adds absolute weight penalty forcing '
                                                                     'coefficients to zero (feature selection); L2 '
                                                                     'adds squared weight penalty shrinking weights '
                                                                     'towards zero',
                                                                     'L2 eliminates features completely while L1 keeps '
                                                                     'all features',
                                                                     'L1 increases model variance while L2 increases '
                                                                     'model bias',
                                                                     'Both penalties work only on decision tree leaf '
                                                                     'nodes'],
                                                      'q': 'How do L1 (Lasso) and L2 (Ridge) Regularization prevent '
                                                           'overfitting, and how do their penalty terms differ in '
                                                           'feature selection?'}],
                          'Python': [   {   'answer': 'NumPy',
                                            'difficulty': 'Basic',
                                            'options': ['NumPy', 'Pandas', 'Scikit-Learn', 'Matplotlib'],
                                            'q': 'Which numerical library provides multi-dimensional array objects '
                                                 '(ndarray) in Python?'},
                                        {   'answer': 'Executing operations on entire arrays in optimized C code '
                                                      'without explicit Python for-loops',
                                            'difficulty': 'Beginner',
                                            'options': [   'Executing operations on entire arrays in optimized C code '
                                                           'without explicit Python for-loops',
                                                           'Converting images into vector graphics format',
                                                           'Replacing floating-point numbers with integer vectors',
                                                           'Sorting arrays using multithreaded queues'],
                                            'q': 'What is Vectorization in NumPy?'},
                                        {   'answer': 'Broadcasting',
                                            'difficulty': 'Intermediate',
                                            'options': ['Broadcasting', 'Reshaping', 'Slicing', 'Concatenation'],
                                            'q': 'What mechanism in NumPy allows array arithmetic operations between '
                                                 'arrays of different shapes?'},
                                        {   'answer': 'It allows slicing and buffer access without copying underlying '
                                                      'memory bytes',
                                            'difficulty': 'Advanced',
                                            'options': [   'It allows slicing and buffer access without copying '
                                                           'underlying memory bytes',
                                                           'It compresses numeric arrays into zip archives in RAM',
                                                           'It offloads memory onto hard drive swap partitions',
                                                           'It converts Python integers to strings'],
                                            'q': 'How does Python handle memory management for large arrays using '
                                                 'memory views (`memoryview`)?'},
                                        {   'answer': 'By dynamically constructing a Directed Acyclic Graph (DAG) of '
                                                      'computations where leaves are input tensors and root is loss',
                                            'difficulty': 'Expert',
                                            'options': [   'By dynamically constructing a Directed Acyclic Graph (DAG) '
                                                           'of computations where leaves are input tensors and root is '
                                                           'loss',
                                                           'By compiling Python code into C++ headers before runtime',
                                                           'By calculating numerical derivatives using finite '
                                                           'difference approximation at every step',
                                                           'By storing matrix values in disk-backed SQL tables'],
                                            'q': 'In deep learning frameworks like PyTorch, how does automatic '
                                                 'differentiation (`autograd`) track operations on Tensors?'}],
                          'Statistics': [   {   'answer': 'Conditional Probability',
                                                'difficulty': 'Basic',
                                                'options': [   'Conditional Probability',
                                                               'Joint Probability',
                                                               'Marginal Probability',
                                                               'Prior Probability'],
                                                'q': 'What is the probability of an event given that another event has '
                                                     'already occurred?'},
                                            {   'answer': "Bayes' Theorem",
                                                'difficulty': 'Beginner',
                                                'options': [   "Bayes' Theorem",
                                                               'Central Limit Theorem',
                                                               "Markov's Inequality",
                                                               'Law of Total Probability'],
                                                'q': 'Which rule calculates posterior probability P(A|B) using prior '
                                                     'probability P(A) and likelihood P(B|A)?'},
                                            {   'answer': 'Poisson Distribution',
                                                'difficulty': 'Intermediate',
                                                'options': [   'Poisson Distribution',
                                                               'Binomial Distribution',
                                                               'Normal Distribution',
                                                               'Uniform Distribution'],
                                                'q': 'Which probability distribution models the number of events '
                                                     'occurring in a fixed interval of time/space given a constant '
                                                     'average rate?'},
                                            {   'answer': 'Maximum Likelihood Estimation (MLE)',
                                                'difficulty': 'Advanced',
                                                'options': [   'Maximum Likelihood Estimation (MLE)',
                                                               'Ordinary Least Squares (OLS)',
                                                               'Gradient Descent',
                                                               'Markov Chain Monte Carlo (MCMC)'],
                                                'q': 'What parameter estimation method finds parameter values that '
                                                     'maximize the likelihood of observing the given sample data?'},
                                            {   'answer': 'It adjusts the significance threshold alpha by dividing it '
                                                          'by the total number of statistical hypothesis tests '
                                                          'performed',
                                                'difficulty': 'Expert',
                                                'options': [   'It adjusts the significance threshold alpha by '
                                                               'dividing it by the total number of statistical '
                                                               'hypothesis tests performed',
                                                               'It increases sample size requirements by 10x',
                                                               'It replaces t-tests with Chi-square goodness-of-fit '
                                                               'tests',
                                                               'It sets p-value cutoff to 0.50'],
                                                'q': 'When conducting A/B testing with multiple concurrent metrics, '
                                                     'how does the Bonferroni Correction prevent inflation of Type I '
                                                     'error (False Positive rate)?'}]},
    'Cloud Computing': {   'AWS': [   {   'answer': 'EC2',
                                          'difficulty': 'Basic',
                                          'options': ['EC2', 'S3', 'RDS', 'Lambda'],
                                          'q': 'Which AWS compute service provides scalable virtual servers in the '
                                               'cloud?'},
                                      {   'answer': 'S3 (Simple Storage Service)',
                                          'difficulty': 'Beginner',
                                          'options': ['S3 (Simple Storage Service)', 'EBS', 'EFS', 'DynamoDB'],
                                          'q': 'Which AWS storage service provides scalable object storage for files '
                                               'and media?'},
                                      {   'answer': 'AWS Lambda',
                                          'difficulty': 'Intermediate',
                                          'options': ['AWS Lambda', 'AWS EC2', 'AWS ECS', 'AWS Fargate'],
                                          'q': 'What AWS serverless service executes code automatically in response to '
                                               'events without provisioning virtual servers?'},
                                      {   'answer': 'ALB distributes incoming HTTP traffic across healthy EC2 '
                                                    'instances while Auto Scaling dynamically provisions/terminates '
                                                    'instances based on CPU/traffic metrics',
                                          'difficulty': 'Advanced',
                                          'options': [   'ALB distributes incoming HTTP traffic across healthy EC2 '
                                                         'instances while Auto Scaling dynamically '
                                                         'provisions/terminates instances based on CPU/traffic metrics',
                                                         'Auto Scaling routes web traffic directly to S3 buckets',
                                                         'ALB increases virtual server RAM without rebooting',
                                                         'AWS Lambda converts static EC2 servers into database tables'],
                                          'q': 'How does AWS Auto Scaling combined with an Application Load Balancer '
                                               '(ALB) handle high traffic spikes?'},
                                      {   'answer': 'Use Route 53 Latency-Based Routing + Aurora Global Database for '
                                                    'cross-region replication + S3 Cross-Region Replication (CRR)',
                                          'difficulty': 'Expert',
                                          'options': [   'Use Route 53 Latency-Based Routing + Aurora Global Database '
                                                         'for cross-region replication + S3 Cross-Region Replication '
                                                         '(CRR)',
                                                         'Run single EC2 instance in us-east-1 and take manual weekly '
                                                         'snapshots',
                                                         'Export raw database dumps to local laptop hard drives daily',
                                                         'Use single-AZ RDS deployments with read replicas'],
                                          'q': 'How do you architect a Multi-Region Active-Active disaster recovery '
                                               'solution on AWS for critical enterprise applications?'}],
                           'Cloud Security': [   {   'answer': 'Shared Responsibility Model',
                                                     'difficulty': 'Basic',
                                                     'options': [   'Shared Responsibility Model',
                                                                    'Zero Trust Architecture',
                                                                    'Defense in Depth',
                                                                    'ISO 27001 Standard'],
                                                     'q': 'What security framework divides security obligations '
                                                          'between the cloud provider (Security OF the cloud) and '
                                                          'customer (Security IN the cloud)?'},
                                                 {   'answer': 'IAM (Identity and Access Management)',
                                                     'difficulty': 'Beginner',
                                                     'options': [   'IAM (Identity and Access Management)',
                                                                    'WAF',
                                                                    'VPC',
                                                                    'KMS'],
                                                     'q': 'Which cloud security control manages user identities, '
                                                          'roles, and granular access permissions?'},
                                                 {   'answer': 'KMS (Key Management Service)',
                                                     'difficulty': 'Intermediate',
                                                     'options': [   'KMS (Key Management Service)',
                                                                    'IAM',
                                                                    'CloudTrail',
                                                                    'GuardDuty'],
                                                     'q': 'What cloud service encrypts and decrypts sensitive data '
                                                          'using managed master encryption keys?'},
                                                 {   'answer': 'By continuously scanning cloud infrastructure '
                                                               'configurations against security benchmarks (CIS) and '
                                                               'compliance frameworks to detect misconfigurations',
                                                     'difficulty': 'Advanced',
                                                     'options': [   'By continuously scanning cloud infrastructure '
                                                                    'configurations against security benchmarks (CIS) '
                                                                    'and compliance frameworks to detect '
                                                                    'misconfigurations',
                                                                    'By installing local antivirus software on '
                                                                    'physical host hypervisors',
                                                                    'By blocking incoming HTTP web traffic at domain '
                                                                    'registrars',
                                                                    'By auto-deleting cloud storage buckets every 30 '
                                                                    'days'],
                                                     'q': 'How does Cloud Security Posture Management (CSPM) protect '
                                                          'multi-cloud enterprise deployments?'},
                                                 {   'answer': 'Deploy NAT Gateways with Egress Proxy Filtering / AWS '
                                                               'Network Firewall and enforce strict VPC Endpoint '
                                                               'Policies for S3/DynamoDB',
                                                     'difficulty': 'Expert',
                                                     'options': [   'Deploy NAT Gateways with Egress Proxy Filtering / '
                                                                    'AWS Network Firewall and enforce strict VPC '
                                                                    'Endpoint Policies for S3/DynamoDB',
                                                                    'Allow open 0.0.0.0/0 inbound security group rules',
                                                                    'Disable SSL encryption on internal microservice '
                                                                    'calls',
                                                                    'Store root credentials in plain text environment '
                                                                    'variables'],
                                                     'q': 'When mitigating data exfiltration risks in public cloud VPC '
                                                          'networks, what network security architecture restricts '
                                                          'outbound traffic?'}],
                           'DevOps': [   {   'answer': 'Continuous Integration (CI)',
                                             'difficulty': 'Basic',
                                             'options': [   'Continuous Integration (CI)',
                                                            'Continuous Deployment (CD)',
                                                            'Infrastructure as Code (IaC)',
                                                            'Monitoring'],
                                             'q': 'What DevOps practice automatically builds, tests, and validates '
                                                  'code changes in a shared repository?'},
                                         {   'answer': 'Docker',
                                             'difficulty': 'Beginner',
                                             'options': ['Docker', 'Kubernetes', 'Jenkins', 'Terraform'],
                                             'q': 'Which containerization platform packages applications and '
                                                  'dependencies into lightweight portable containers?'},
                                         {   'answer': 'Terraform',
                                             'difficulty': 'Intermediate',
                                             'options': ['Terraform', 'Docker', 'Ansible', 'Git'],
                                             'q': 'Which Infrastructure as Code (IaC) tool uses declarative '
                                                  'configuration files to provision multi-cloud resources?'},
                                         {   'answer': 'Blue-Green switches 100% traffic instantly between two '
                                                       'identical environments; Canary gradually shifts a small '
                                                       'percentage of traffic to the new version',
                                             'difficulty': 'Advanced',
                                             'options': [   'Blue-Green switches 100% traffic instantly between two '
                                                            'identical environments; Canary gradually shifts a small '
                                                            'percentage of traffic to the new version',
                                                            'Canary deployment wipes the database before release; '
                                                            'Blue-Green keeps old data',
                                                            'Blue-Green applies only to mobile apps; Canary applies to '
                                                            'backend APIs',
                                                            'There is no operational difference'],
                                             'q': 'What is the key difference between Blue-Green Deployment and Canary '
                                                  'Deployment strategies?'},
                                         {   'answer': 'It treats Git repositories as single source of truth; '
                                                       'controllers continuously monitor Git commits and sync actual '
                                                       'cluster state to match target manifests',
                                             'difficulty': 'Expert',
                                             'options': [   'It treats Git repositories as single source of truth; '
                                                            'controllers continuously monitor Git commits and sync '
                                                            'actual cluster state to match target manifests',
                                                            'It executes manual `kubectl apply` commands via developer '
                                                            'SSH terminals',
                                                            'It rebuilds physical server host hardware on every code '
                                                            'push',
                                                            'It stores production container passwords in public Git '
                                                            'commits'],
                                             'q': 'How does GitOps (e.g. ArgoCD / Flux) enforce continuous state '
                                                  'reconciliation for Kubernetes container clusters?'}],
                           'Linux': [   {   'answer': 'pwd',
                                            'difficulty': 'Basic',
                                            'options': ['pwd', 'ls', 'cd', 'dir'],
                                            'q': 'Which Linux command displays the current working directory path?'},
                                        {   'answer': 'chmod',
                                            'difficulty': 'Beginner',
                                            'options': ['chmod', 'chown', 'chgrp', 'sudo'],
                                            'q': 'Which Linux command changes file and directory permissions?'},
                                        {   'answer': '755',
                                            'difficulty': 'Intermediate',
                                            'options': ['755', '644', '777', '700'],
                                            'q': 'What numeric permission representation grants Read, Write, and '
                                                 'Execute (rwx) to Owner, and Read/Execute (r-x) to Group and Others?'},
                                        {   'answer': 'ps aux | grep process_name',
                                            'difficulty': 'Advanced',
                                            'options': [   'ps aux | grep process_name',
                                                           'cat /etc/processes | find process_name',
                                                           'top --search process_name',
                                                           'ls -la /proc | filter process_name'],
                                            'q': 'Which Linux command pipeline filters running system processes by '
                                                 'name?'},
                                        {   'answer': 'cgroups restrict and meter hardware resource usage (CPU, RAM, '
                                                      'I/O); namespaces isolate system view (Process IDs, Mounts, '
                                                      'Network interfaces)',
                                            'difficulty': 'Expert',
                                            'options': [   'cgroups restrict and meter hardware resource usage (CPU, '
                                                           'RAM, I/O); namespaces isolate system view (Process IDs, '
                                                           'Mounts, Network interfaces)',
                                                           'cgroups compile C source code; namespaces handle SSH '
                                                           'logins',
                                                           'cgroups format hard drives; namespaces assign domain names',
                                                           'cgroups compress system logs; namespaces manage user '
                                                           'passwords'],
                                            'q': 'How do Linux cgroups (Control Groups) and namespaces provide '
                                                 'foundational isolation for container runtimes (Docker/containerd)?'}],
                           'Networking': [   {   'answer': 'DNS (Domain Name System)',
                                                 'difficulty': 'Basic',
                                                 'options': ['DNS (Domain Name System)', 'DHCP', 'NAT', 'BGP'],
                                                 'q': 'What service maps human-readable domain names (e.g. '
                                                      '`example.com`) to numeric IP addresses?'},
                                             {   'answer': 'VPC (Virtual Private Cloud)',
                                                 'difficulty': 'Beginner',
                                                 'options': ['VPC (Virtual Private Cloud)', 'VPN', 'WAN', 'LAN'],
                                                 'q': 'What networking technology isolates cloud resources within a '
                                                      'private virtual network segment?'},
                                             {   'answer': '254',
                                                 'difficulty': 'Intermediate',
                                                 'options': ['254', '512', '128', '64'],
                                                 'q': 'In CIDR network notation, how many usable IP addresses are '
                                                      'available in a `/24` subnet?'},
                                             {   'answer': 'Security Groups evaluate return traffic automatically '
                                                           '(stateful); NACLs require explicit inbound and outbound '
                                                           'rules (stateless) processed by rule order',
                                                 'difficulty': 'Advanced',
                                                 'options': [   'Security Groups evaluate return traffic automatically '
                                                                '(stateful); NACLs require explicit inbound and '
                                                                'outbound rules (stateless) processed by rule order',
                                                                'NACLs apply to individual EC2 instances; Security '
                                                                'Groups apply to subnets',
                                                                'Security Groups block IP addresses; NACLs block '
                                                                'domain names',
                                                                'NACLs work only on IPv6 traffic'],
                                                 'q': 'What is the operational difference between a Stateful Security '
                                                      'Group and a Stateless Network ACL (NACL) in cloud VPCs?'},
                                             {   'answer': 'By caching static assets at global Edge Locations close to '
                                                           'users and establishing persistent TLS connection pools to '
                                                           'origin servers',
                                                 'difficulty': 'Expert',
                                                 'options': [   'By caching static assets at global Edge Locations '
                                                                'close to users and establishing persistent TLS '
                                                                'connection pools to origin servers',
                                                                'By compressing database tables into ZIP files before '
                                                                'transmission',
                                                                'By executing web server code directly inside client '
                                                                'browser engines',
                                                                'By replacing TCP packets with UDP datagrams globally'],
                                                 'q': 'How does a Content Delivery Network (CDN, e.g. CloudFront) '
                                                      'optimize dynamic API latency and static asset delivery '
                                                      'globally?'}]},
    'Cyber Security Analyst': {   'C': [   {   'answer': '&',
                                               'difficulty': 'Basic',
                                               'options': ['&', '*', '->', '%'],
                                               'q': 'Which operator returns the memory address of a variable in C?'},
                                           {   'answer': '<stdio.h>',
                                               'difficulty': 'Beginner',
                                               'options': ['<stdio.h>', '<stdlib.h>', '<string.h>', '<math.h>'],
                                               'q': 'What header file must be included to use functions like '
                                                    '`printf()` and `scanf()` in C?'},
                                           {   'answer': 'strcpy()',
                                               'difficulty': 'Intermediate',
                                               'options': ['strcpy()', 'strncpy()', 'snprintf()', 'memcpy()'],
                                               'q': 'What unsafe C library string function is notoriously vulnerable '
                                                    'to buffer overflows because it lacks string length bounds '
                                                    'checking?'},
                                           {   'answer': 'Stack Canaries detect stack corruption before function '
                                                         'return; ASLR randomizes memory addresses of '
                                                         'stack/heap/libraries',
                                               'difficulty': 'Advanced',
                                               'options': [   'Stack Canaries detect stack corruption before function '
                                                              'return; ASLR randomizes memory addresses of '
                                                              'stack/heap/libraries',
                                                              'They convert C source code into Python scripts before '
                                                              'execution',
                                                              'They disable pointer dereferencing in memory',
                                                              'They limit C arrays to 10 elements max'],
                                               'q': 'How do modern compilers and operating systems mitigate C buffer '
                                                    'overflow attacks using Stack Canaries and ASLR?'},
                                           {   'answer': 'Accessing memory via a pointer after calling `free()` causes '
                                                         'undefined behavior; prevented by setting pointers to NULL '
                                                         'immediately after freeing',
                                               'difficulty': 'Expert',
                                               'options': [   'Accessing memory via a pointer after calling `free()` '
                                                              'causes undefined behavior; prevented by setting '
                                                              'pointers to NULL immediately after freeing',
                                                              'Calling `malloc()` twice on the same variable; '
                                                              'prevented by using `realloc()`',
                                                              'Writing to read-only global constants; prevented by '
                                                              '`const` keyword',
                                                              'Dereferencing NULL pointers; prevented by '
                                                              '`try...except`'],
                                               'q': 'How does a Use-After-Free (UAF) vulnerability manifest in C '
                                                    'pointer management, and how can defensive programming prevent '
                                                    'it?'}],
                                  'C++': [   {   'answer': 'private',
                                                 'difficulty': 'Basic',
                                                 'options': ['private', 'public', 'protected', 'friend'],
                                                 'q': 'Which access modifier restricts C++ class members so they are '
                                                      'accessible only within the defining class?'},
                                             {   'answer': 'Exception Handling',
                                                 'difficulty': 'Beginner',
                                                 'options': ['Exception Handling', 'Templates', 'RTI', 'Signals'],
                                                 'q': 'Which C++ feature handles unexpected runtime errors in a '
                                                      'structured manner using `try`, `catch`, and `throw`?'},
                                             {   'answer': 'Resource allocation is tied to object lifetime so resource '
                                                           'cleanup occurs automatically in destructors when objects '
                                                           'leave scope',
                                                 'difficulty': 'Intermediate',
                                                 'options': [   'Resource allocation is tied to object lifetime so '
                                                                'resource cleanup occurs automatically in destructors '
                                                                'when objects leave scope',
                                                                'Resources are initialized lazily upon first method '
                                                                'invocation',
                                                                'Memory garbage collection runs every 5 milliseconds',
                                                                'Global pointers manage allocated memory blocks'],
                                                 'q': 'How does RAII (Resource Acquisition Is Initialization) prevent '
                                                      'resource leaks in secure C++ development?'},
                                             {   'answer': 'Vtable Hijacking / Control Flow Hijacking, where '
                                                           'redirected function pointers execute arbitrary code',
                                                 'difficulty': 'Advanced',
                                                 'options': [   'Vtable Hijacking / Control Flow Hijacking, where '
                                                                'redirected function pointers execute arbitrary code',
                                                                'Template instantiation deadlock',
                                                                'Stack overflow error in main loop',
                                                                'Memory leak in static objects'],
                                                 'q': 'What C++ memory safety issue occurs when virtual function '
                                                      'tables (vtables) are corrupted by memory overwrites?'},
                                             {   'answer': 'DEP/NX prevents executing code in data segments '
                                                           '(stack/heap); CFG validates indirect function call targets '
                                                           'before branching',
                                                 'difficulty': 'Expert',
                                                 'options': [   'DEP/NX prevents executing code in data segments '
                                                                '(stack/heap); CFG validates indirect function call '
                                                                'targets before branching',
                                                                'DEP/NX encrypts hard drives; CFG scans incoming '
                                                                'network packets',
                                                                'DEP/NX restricts class inheritance; CFG checks '
                                                                'standard library templates',
                                                                'DEP/NX disables multi-threading; CFG blocks C++ '
                                                                'compiler warnings'],
                                                 'q': 'How do compiler exploit mitigations like DEP / NX bit and '
                                                      'Control Flow Guard (CFG) defend C++ applications?'}],
                                  'Computer Network': [   {   'answer': '7',
                                                              'difficulty': 'Basic',
                                                              'options': ['7', '4', '5', '6'],
                                                              'q': 'How many layers are in the OSI (Open Systems '
                                                                   'Interconnection) reference model?'},
                                                          {   'answer': 'ARP',
                                                              'difficulty': 'Beginner',
                                                              'options': ['ARP', 'DNS', 'DHCP', 'ICMP'],
                                                              'q': 'Which protocol resolves IP addresses to MAC '
                                                                   'addresses on a local local network?'},
                                                          {   'answer': 'SYN -> SYN-ACK -> ACK',
                                                              'difficulty': 'Intermediate',
                                                              'options': [   'SYN -> SYN-ACK -> ACK',
                                                                             'SYN -> ACK -> FIN',
                                                                             'FIN -> ACK -> RST',
                                                                             'ACK -> SYN-ACK -> SYN'],
                                                              'q': 'What TCP 3-Way Handshake flag sequence establishes '
                                                                   'a connection between client and server?'},
                                                          {   'answer': 'Sliding Window Protocol and Acknowledgments '
                                                                        'with Retransmission Timers',
                                                              'difficulty': 'Advanced',
                                                              'options': [   'Sliding Window Protocol and '
                                                                             'Acknowledgments with Retransmission '
                                                                             'Timers',
                                                                             'UDP Datagram Checksums',
                                                                             'BGP Route Advertisements',
                                                                             'ICMP Echo Requests'],
                                                              'q': 'What mechanism in TCP provides reliability and '
                                                                   'flow control to prevent sender from overwhelming '
                                                                   'receiver?'},
                                                          {   'answer': 'Rogue Autonomous Systems announce '
                                                                        'unauthorized IP prefixes diverting traffic; '
                                                                        'mitigated by RPKI (Resource Public Key '
                                                                        'Infrastructure)',
                                                              'difficulty': 'Expert',
                                                              'options': [   'Rogue Autonomous Systems announce '
                                                                             'unauthorized IP prefixes diverting '
                                                                             'traffic; mitigated by RPKI (Resource '
                                                                             'Public Key Infrastructure)',
                                                                             'Attackers flood DNS resolvers with UDP '
                                                                             'packets; mitigated by DNSSEC',
                                                                             'Routers drop TCP packets with invalid '
                                                                             'checksums; mitigated by IPsec',
                                                                             'MAC addresses are spoofed on Wi-Fi APs; '
                                                                             'mitigated by WPA3'],
                                                              'q': 'How does BGP Route Hijacking disrupt global '
                                                                   'internet traffic, and what defense mechanism '
                                                                   'mitigates it?'}],
                                  'Cryptography': [   {   'answer': 'Symmetric Encryption',
                                                          'difficulty': 'Basic',
                                                          'options': [   'Symmetric Encryption',
                                                                         'Asymmetric Encryption',
                                                                         'Hashing',
                                                                         'Digital Signature'],
                                                          'q': 'Which cryptographic algorithm type uses the same key '
                                                               'for both encryption and decryption?'},
                                                      {   'answer': 'SHA-256',
                                                          'difficulty': 'Beginner',
                                                          'options': [   'SHA-256',
                                                                         'AES-256',
                                                                         'RSA-2048',
                                                                         'Diffie-Hellman'],
                                                          'q': 'Which algorithm is a widely used cryptographic hash '
                                                               'function producing a 256-bit hash digest?'},
                                                      {   'answer': 'Digital certificates issued and cryptographically '
                                                                    'signed by trusted Certificate Authorities (CAs) '
                                                                    'bind public keys to domain identities',
                                                          'difficulty': 'Intermediate',
                                                          'options': [   'Digital certificates issued and '
                                                                         'cryptographically signed by trusted '
                                                                         'Certificate Authorities (CAs) bind public '
                                                                         'keys to domain identities',
                                                                         'Servers send private keys to client web '
                                                                         'browsers over plain HTTP',
                                                                         'DNS servers encrypt web traffic using '
                                                                         'symmetric keys',
                                                                         'Browsers generate random passwords for '
                                                                         'website hosts'],
                                                          'q': 'How does Public Key Infrastructure (PKI) establish '
                                                               'trust for SSL/TLS HTTPS website connections?'},
                                                      {   'answer': 'The computational difficulty of calculating '
                                                                    'Discrete Logarithms over finite fields',
                                                          'difficulty': 'Advanced',
                                                          'options': [   'The computational difficulty of calculating '
                                                                         'Discrete Logarithms over finite fields',
                                                                         'The impossibility of multiplying prime '
                                                                         'numbers',
                                                                         'The speed of symmetric AES encryption',
                                                                         'The properties of XOR bitwise operation on '
                                                                         'strings'],
                                                          'q': 'What mathematical property enables Diffie-Hellman Key '
                                                               'Exchange to securely establish a shared secret over an '
                                                               'insecure channel?'},
                                                      {   'answer': "Shor's Algorithm on quantum computers efficiently "
                                                                    'solves prime factorization and discrete logs; '
                                                                    'mitigated by Post-Quantum Cryptography (PQC)',
                                                          'difficulty': 'Expert',
                                                          'options': [   "Shor's Algorithm on quantum computers "
                                                                         'efficiently solves prime factorization and '
                                                                         'discrete logs; mitigated by Post-Quantum '
                                                                         'Cryptography (PQC)',
                                                                         "Grover's Algorithm deletes cryptographic "
                                                                         'keys from server memory; mitigated by '
                                                                         'firewalls',
                                                                         'Quantum computers disable SHA-256 hash '
                                                                         'digests; mitigated by password complexity',
                                                                         'Quantum computers bypass TLS firewalls; '
                                                                         'mitigated by physical locks'],
                                                          'q': 'Why are quantum computers poised to break RSA and ECC '
                                                               'encryption, and what cryptographic paradigm addresses '
                                                               'this threat?'}],
                                  'Cyber Security Fundamentals': [   {   'answer': 'Confidentiality, Integrity, '
                                                                                   'Availability',
                                                                         'difficulty': 'Basic',
                                                                         'options': [   'Confidentiality, Integrity, '
                                                                                        'Availability',
                                                                                        'Control, Inspection, '
                                                                                        'Authentication',
                                                                                        'Cipher, Information, '
                                                                                        'Authorization',
                                                                                        'Compliance, Isolation, Audit'],
                                                                         'q': 'What three core security principles '
                                                                              'make up the CIA Triad?'},
                                                                     {   'answer': 'Defense in Depth',
                                                                         'difficulty': 'Beginner',
                                                                         'options': [   'Defense in Depth',
                                                                                        'Single Point of Failure',
                                                                                        'Air Gapping',
                                                                                        'Least Privilege'],
                                                                         'q': 'What security strategy deploys multiple '
                                                                              'overlapping defensive controls across '
                                                                              'an IT infrastructure?'},
                                                                     {   'answer': 'Principle of Least Privilege',
                                                                         'difficulty': 'Intermediate',
                                                                         'options': [   'Principle of Least Privilege',
                                                                                        'Separation of Duties',
                                                                                        'Need to Know',
                                                                                        'Zero Trust'],
                                                                         'q': 'What principle dictates that users and '
                                                                              'processes should be granted only the '
                                                                              'minimum access rights necessary to '
                                                                              'perform their job?'},
                                                                     {   'answer': 'Zero Trust assumes no implicit '
                                                                                   'trust inside or outside the '
                                                                                   'network, requiring continuous '
                                                                                   'authentication, authorization, and '
                                                                                   'micro-segmentation',
                                                                         'difficulty': 'Advanced',
                                                                         'options': [   'Zero Trust assumes no '
                                                                                        'implicit trust inside or '
                                                                                        'outside the network, '
                                                                                        'requiring continuous '
                                                                                        'authentication, '
                                                                                        'authorization, and '
                                                                                        'micro-segmentation',
                                                                                        'Zero Trust relies entirely on '
                                                                                        'external network firewalls',
                                                                                        'Zero Trust allows all '
                                                                                        'internal IP addresses full '
                                                                                        'access without credentials',
                                                                                        'Zero Trust disables '
                                                                                        'multi-factor authentication'],
                                                                         'q': 'How does a Zero Trust Security Model '
                                                                              'fundamentally differ from traditional '
                                                                              'Perimeter-based (Castle-and-Moat) '
                                                                              'security?'},
                                                                     {   'answer': 'Preparation -> Detection & '
                                                                                   'Analysis -> Containment, '
                                                                                   'Eradication & Recovery -> '
                                                                                   'Post-Incident Activity',
                                                                         'difficulty': 'Expert',
                                                                         'options': [   'Preparation -> Detection & '
                                                                                        'Analysis -> Containment, '
                                                                                        'Eradication & Recovery -> '
                                                                                        'Post-Incident Activity',
                                                                                        'Containment -> Eradication -> '
                                                                                        'Password Reset -> Firing '
                                                                                        'Staff',
                                                                                        'Detection -> Legal '
                                                                                        'Notification -> Encryption -> '
                                                                                        'Backup Wipe',
                                                                                        'Reconnaissance -> Scanning -> '
                                                                                        'Exploitation -> Cleanup'],
                                                                         'q': 'When responding to an ongoing '
                                                                              'enterprise security breach, what are '
                                                                              'the primary sequential phases of an '
                                                                              'Incident Response Plan (NIST SP '
                                                                              '800-61)?'}],
                                  'Database Management': [   {   'answer': 'SQL Injection (SQLi)',
                                                                 'difficulty': 'Basic',
                                                                 'options': [   'SQL Injection (SQLi)',
                                                                                'Cross-Site Scripting (XSS)',
                                                                                'Buffer Overflow',
                                                                                'Command Injection'],
                                                                 'q': 'What security vulnerability occurs when '
                                                                      'untrusted user input is directly concatenated '
                                                                      'into a database SQL query string?'},
                                                             {   'answer': 'Using Parameterized Queries (Prepared '
                                                                           'Statements)',
                                                                 'difficulty': 'Beginner',
                                                                 'options': [   'Using Parameterized Queries (Prepared '
                                                                                'Statements)',
                                                                                'Client-side JavaScript form '
                                                                                'validation',
                                                                                'Encrypting database hard drives',
                                                                                'Changing default database port '
                                                                                'numbers'],
                                                                 'q': 'Which defense technique is most effective at '
                                                                      'preventing SQL Injection vulnerabilities?'},
                                                             {   'answer': 'Durability',
                                                                 'difficulty': 'Intermediate',
                                                                 'options': [   'Durability',
                                                                                'Atomicity',
                                                                                'Consistency',
                                                                                'Isolation'],
                                                                 'q': 'What ACID database property guarantees that '
                                                                      'committed transactions are permanently saved '
                                                                      'even during power failure?'},
                                                             {   'answer': 'Permissions to SELECT, INSERT, UPDATE, or '
                                                                           'DELETE specific tables/views are granted '
                                                                           'to predefined roles rather than individual '
                                                                           'users',
                                                                 'difficulty': 'Advanced',
                                                                 'options': [   'Permissions to SELECT, INSERT, '
                                                                                'UPDATE, or DELETE specific '
                                                                                'tables/views are granted to '
                                                                                'predefined roles rather than '
                                                                                'individual users',
                                                                                'Users are assigned full DBA admin '
                                                                                'privileges by default',
                                                                                'SQL queries are checked against '
                                                                                'antivirus databases',
                                                                                'Database logs are encrypted using '
                                                                                'browser cookies'],
                                                                 'q': 'How does Database Role-Based Access Control '
                                                                      '(RBAC) enforce security compliance?'},
                                                             {   'answer': 'By encrypting database files, logs, and '
                                                                           'backups on disk using symmetric keys '
                                                                           '(AES-256) managed via a Hardware Security '
                                                                           'Module (HSM)',
                                                                 'difficulty': 'Expert',
                                                                 'options': [   'By encrypting database files, logs, '
                                                                                'and backups on disk using symmetric '
                                                                                'keys (AES-256) managed via a Hardware '
                                                                                'Security Module (HSM)',
                                                                                'By placing SSL certificates on web '
                                                                                'server frontends',
                                                                                'By hashing user passwords with Base64 '
                                                                                'encoding',
                                                                                'By storing database files on '
                                                                                'read-only optical discs'],
                                                                 'q': 'How do database security engineers implement '
                                                                      'Encryption at Rest and Transparent Data '
                                                                      'Encryption (TDE)?'}],
                                  'Ethical Hacking': [   {   'answer': 'Reconnaissance / Footprinting',
                                                             'difficulty': 'Basic',
                                                             'options': [   'Reconnaissance / Footprinting',
                                                                            'Exploitation',
                                                                            'Privilege Escalation',
                                                                            'Maintaining Access'],
                                                             'q': 'What is the initial passive phase of a penetration '
                                                                  'test where information is gathered about a target '
                                                                  'organization?'},
                                                         {   'answer': 'Nmap',
                                                             'difficulty': 'Beginner',
                                                             'options': [   'Nmap',
                                                                            'Wireshark',
                                                                            'Metasploit',
                                                                            'Burp Suite'],
                                                             'q': 'Which open-source tool is widely used for network '
                                                                  'discovery, port scanning, and OS detection?'},
                                                         {   'answer': 'Phishing',
                                                             'difficulty': 'Intermediate',
                                                             'options': [   'Phishing',
                                                                            'Man-in-the-Middle',
                                                                            'SQL Injection',
                                                                            'Buffer Overflow'],
                                                             'q': 'What type of attack tricks users into revealing '
                                                                  'sensitive credentials by sending deceptive emails '
                                                                  'mimicking trusted organizations?'},
                                                         {   'answer': 'By performing static code analysis (SAST), '
                                                                       'dynamic application scanning (DAST), manual '
                                                                       'penetration testing, and reviewing access '
                                                                       'boundaries',
                                                             'difficulty': 'Advanced',
                                                             'options': [   'By performing static code analysis '
                                                                            '(SAST), dynamic application scanning '
                                                                            '(DAST), manual penetration testing, and '
                                                                            'reviewing access boundaries',
                                                                            'By running antivirus software on database '
                                                                            'servers',
                                                                            'By setting server passwords to change '
                                                                            'every 24 hours',
                                                                            'By disabling HTTP GET requests'],
                                                             'q': 'How do web application security teams '
                                                                  'systematically audit applications against the OWASP '
                                                                  'Top 10 vulnerabilities (e.g., Broken Access '
                                                                  'Control, Injection)?'},
                                                         {   'answer': 'Enforce network micro-segmentation, restrict '
                                                                       'local admin rights, disable LSASS memory '
                                                                       'dumping, and monitor Kerberos ticket requests '
                                                                       '(Kerberoasting)',
                                                             'difficulty': 'Expert',
                                                             'options': [   'Enforce network micro-segmentation, '
                                                                            'restrict local admin rights, disable '
                                                                            'LSASS memory dumping, and monitor '
                                                                            'Kerberos ticket requests (Kerberoasting)',
                                                                            'Install dual firewalls on external '
                                                                            'routers',
                                                                            'Change external domain DNS records',
                                                                            'Convert domain controllers to Linux web '
                                                                            'servers'],
                                                             'q': 'How do security teams secure enterprise '
                                                                  'environments against lateral movement following an '
                                                                  'initial endpoint compromise?'}],
                                  'Java': [   {   'answer': 'JVM (Java Virtual Machine)',
                                                  'difficulty': 'Basic',
                                                  'options': [   'JVM (Java Virtual Machine)',
                                                                 'JDK',
                                                                 'JRE',
                                                                 'JIT Compiler'],
                                                  'q': 'What environment executes Java bytecode on target operating '
                                                       'systems?'},
                                              {   'answer': 'final',
                                                  'difficulty': 'Beginner',
                                                  'options': ['final', 'static', 'const', 'immutable'],
                                                  'q': 'Which Java keyword prevents a variable value from being '
                                                       'modified once initialized?'},
                                              {   'answer': 'JNDI Injection leading to Remote Code Execution (RCE) via '
                                                            'untrusted log string lookup',
                                                  'difficulty': 'Intermediate',
                                                  'options': [   'JNDI Injection leading to Remote Code Execution '
                                                                 '(RCE) via untrusted log string lookup',
                                                                 'SQL Injection in database logging appenders',
                                                                 'Buffer overflow in Log4j C++ native extensions',
                                                                 'Cross-Site Request Forgery in admin UI'],
                                                  'q': 'What security threat vulnerability famously affected the '
                                                       'Apache Log4j Java logging library (Log4Shell)?'},
                                              {   'answer': 'By checking call stack permissions against defined '
                                                            'Security Policy files before performing file, socket, or '
                                                            'process operations',
                                                  'difficulty': 'Advanced',
                                                  'options': [   'By checking call stack permissions against defined '
                                                                 'Security Policy files before performing file, '
                                                                 'socket, or process operations',
                                                                 'By compiling Java bytecode to native assembly before '
                                                                 'execution',
                                                                 'By disabling multi-threading in untrusted applets',
                                                                 'By encrypting class files on disk'],
                                                  'q': 'How does Java Security Manager / AccessController enforce '
                                                       'fine-grained sandbox permissions for untrusted code?'},
                                              {   'answer': 'Disable `DOCTYPE` declarations and external general '
                                                            'entities '
                                                            '(`setFeature("http://apache.org/xml/features/disallow-doctype-decl", '
                                                            'true)`)',
                                                  'difficulty': 'Expert',
                                                  'options': [   'Disable `DOCTYPE` declarations and external general '
                                                                 'entities '
                                                                 '(`setFeature("http://apache.org/xml/features/disallow-doctype-decl", '
                                                                 'true)`)',
                                                                 'Convert XML files to CSV format before parsing',
                                                                 'Parse XML documents using regex match strings',
                                                                 'Encrypt XML request bodies with RSA public keys'],
                                                  'q': 'How do enterprise Java applications defend against XML '
                                                       'External Entity (XXE) attacks during XML parsing?'}],
                                  'OS': [   {   'answer': 'Kernel',
                                                'difficulty': 'Basic',
                                                'options': ['Kernel', 'Shell', 'Compiler', 'File System'],
                                                'q': 'What core component of an Operating System acts as the bridge '
                                                     'between hardware and software application software?'},
                                            {   'answer': 'Blocked / Waiting',
                                                'difficulty': 'Beginner',
                                                'options': ['Blocked / Waiting', 'Running', 'Ready', 'Terminated'],
                                                'q': 'Which CPU scheduling state indicates a process is waiting for an '
                                                     'I/O operation to complete?'},
                                            {   'answer': 'Deadlock',
                                                'difficulty': 'Intermediate',
                                                'options': [   'Deadlock',
                                                               'Race Condition',
                                                               'Starvation',
                                                               'Context Switch'],
                                                'q': 'What condition occurs when two or more processes are permanently '
                                                     'blocked waiting for resources held by each other?'},
                                            {   'answer': 'It maps non-contiguous physical RAM pages into contiguous '
                                                          'virtual address space; a Page Fault triggers when '
                                                          "referenced page isn't in RAM",
                                                'difficulty': 'Advanced',
                                                'options': [   'It maps non-contiguous physical RAM pages into '
                                                               'contiguous virtual address space; a Page Fault '
                                                               "triggers when referenced page isn't in RAM",
                                                               'It allocates contiguous physical RAM to every process; '
                                                               'Page Fault occurs on CPU overheat',
                                                               'It encrypts process RAM; Page Fault happens on invalid '
                                                               'password entry',
                                                               'It disables swap space; Page Fault occurs on system '
                                                               'shutdown'],
                                                'q': 'How does Virtual Memory Paging prevent memory fragmentation, and '
                                                     'what causes a Page Fault?'},
                                            {   'answer': 'Ring 0 grants direct access to execution instructions and '
                                                          'memory; User applications run in Ring 3 requiring System '
                                                          'Calls (`syscall`) to access hardware',
                                                'difficulty': 'Expert',
                                                'options': [   'Ring 0 grants direct access to execution instructions '
                                                               'and memory; User applications run in Ring 3 requiring '
                                                               'System Calls (`syscall`) to access hardware',
                                                               'Ring 3 controls hardware drivers while Ring 0 runs web '
                                                               'browsers',
                                                               'Ring 0 disables interrupt handlers permanently',
                                                               'Privilege rings are defined in software text files'],
                                                'q': 'How do operating system kernels enforce hardware privilege '
                                                     'separation via Supervisor Mode (Ring 0) vs User Mode (Ring 3)?'}],
                                  'Python': [   {   'answer': 'ssl',
                                                    'difficulty': 'Basic',
                                                    'options': ['ssl', 'socket', 'http', 'crypto'],
                                                    'q': 'Which standard library module in Python handles SSL/TLS '
                                                         'encrypted network sockets?'},
                                                {   'answer': 'requests',
                                                    'difficulty': 'Beginner',
                                                    'options': ['requests', 'urllib', 'http.client', 'flask'],
                                                    'q': 'Which Python library is widely used for sending HTTP '
                                                         'requests in security automation scripts?'},
                                                {   'answer': 'Arbitrary Code Execution via `__reduce__` magic method '
                                                              'during unpickling',
                                                    'difficulty': 'Intermediate',
                                                    'options': [   'Arbitrary Code Execution via `__reduce__` magic '
                                                                   'method during unpickling',
                                                                   'Database table deletion via SQL injection',
                                                                   'Cross-Site Scripting in web browsers',
                                                                   'Memory leak in Python virtual environment'],
                                                    'q': 'What security risk arises from deserializing untrusted user '
                                                         "input using Python's `pickle` module?"},
                                                {   'answer': 'Hash passwords with bcrypt/Argon2id and compare hashes '
                                                              'using constant-time comparison `hmac.compare_digest()`',
                                                    'difficulty': 'Advanced',
                                                    'options': [   'Hash passwords with bcrypt/Argon2id and compare '
                                                                   'hashes using constant-time comparison '
                                                                   '`hmac.compare_digest()`',
                                                                   'Compare plaintext strings using `==` operator',
                                                                   'Store passwords encrypted with Base64 in JSON '
                                                                   'files',
                                                                   'Hash passwords using simple MD5 algorithms'],
                                                    'q': 'How should secure Python applications handle password '
                                                         'storage and comparison to prevent timing attacks?'},
                                                {   'answer': 'Pass command arguments as a list of strings with '
                                                              '`shell=False` to prevent shell parser interpretation',
                                                    'difficulty': 'Expert',
                                                    'options': [   'Pass command arguments as a list of strings with '
                                                                   '`shell=False` to prevent shell parser '
                                                                   'interpretation',
                                                                   'Execute shell strings using `shell=True` combined '
                                                                   'with `eval()`',
                                                                   'Concat user input directly into `os.system()` '
                                                                   'calls',
                                                                   'Encode command strings into HTML escape sequences'],
                                                    'q': "How do security automation frameworks use Python's "
                                                         '`subprocess` module defensively while avoiding Command '
                                                         'Injection?'}],
                                  'Vulnerability Assessment': [   {   'answer': 'CVSS (Common Vulnerability Scoring '
                                                                                'System)',
                                                                      'difficulty': 'Basic',
                                                                      'options': [   'CVSS (Common Vulnerability '
                                                                                     'Scoring System)',
                                                                                     'CVE',
                                                                                     'CWE',
                                                                                     'NIST'],
                                                                      'q': 'What standardized metric system rates the '
                                                                           'severity of IT security vulnerabilities on '
                                                                           'a scale from 0.0 to 10.0?'},
                                                                  {   'answer': 'Nessus',
                                                                      'difficulty': 'Beginner',
                                                                      'options': [   'Nessus',
                                                                                     'Wireshark',
                                                                                     'John the Ripper',
                                                                                     'Hydra'],
                                                                      'q': 'Which tool is commonly utilized for '
                                                                           'automated vulnerability scanning of '
                                                                           'infrastructure and software assets?'},
                                                                  {   'answer': 'A Vulnerability Assessment identifies '
                                                                                'and lists potential security flaws; a '
                                                                                'Penetration Test actively attempts to '
                                                                                'exploit them to verify risk',
                                                                      'difficulty': 'Intermediate',
                                                                      'options': [   'A Vulnerability Assessment '
                                                                                     'identifies and lists potential '
                                                                                     'security flaws; a Penetration '
                                                                                     'Test actively attempts to '
                                                                                     'exploit them to verify risk',
                                                                                     'Vulnerability assessment is '
                                                                                     'illegal while penetration '
                                                                                     'testing is legal',
                                                                                     'Vulnerability assessment tests '
                                                                                     'hardware only; penetration '
                                                                                     'testing tests software',
                                                                                     'There is no difference'],
                                                                      'q': 'What is the primary difference between a '
                                                                           'Vulnerability Assessment and a Penetration '
                                                                           'Test?'},
                                                                  {   'answer': 'Attack Vector (AV), Attack Complexity '
                                                                                '(AC), Privileges Required (PR), and '
                                                                                'User Interaction (UI)',
                                                                      'difficulty': 'Advanced',
                                                                      'options': [   'Attack Vector (AV), Attack '
                                                                                     'Complexity (AC), Privileges '
                                                                                     'Required (PR), and User '
                                                                                     'Interaction (UI)',
                                                                                     'Confidentiality, Integrity, and '
                                                                                     'Availability Impact',
                                                                                     'Remediation Level and Report '
                                                                                     'Confidence',
                                                                                     'Financial Cost and Data Size'],
                                                                      'q': 'What CVSS v3.1 metrics define the '
                                                                           'Exploitability Subscore of a '
                                                                           'vulnerability?'},
                                                                  {   'answer': 'Integrate automated '
                                                                                'SAST/DAST/Container scanning, '
                                                                                'establish SLA-driven patching '
                                                                                'criteria by CVSS score, and track '
                                                                                'remediation via automated ticketers',
                                                                      'difficulty': 'Expert',
                                                                      'options': [   'Integrate automated '
                                                                                     'SAST/DAST/Container scanning, '
                                                                                     'establish SLA-driven patching '
                                                                                     'criteria by CVSS score, and '
                                                                                     'track remediation via automated '
                                                                                     'ticketers',
                                                                                     'Scan production servers manually '
                                                                                     'once per year',
                                                                                     'Ignore low and medium severity '
                                                                                     'vulnerabilities permanently',
                                                                                     'Block all software releases '
                                                                                     'until zero vulnerabilities exist '
                                                                                     'in third-party libraries'],
                                                                      'q': 'How do security teams establish a scalable '
                                                                           'Vulnerability Management Lifecycle in a '
                                                                           'DevSecOps CI/CD pipeline?'}]},
    'Data Analyst': {   'Excel': [   {   'answer': 'VLOOKUP',
                                         'difficulty': 'Basic',
                                         'options': ['HLOOKUP', 'VLOOKUP', 'CONCATENATE', 'COUNTIF'],
                                         'q': 'Which Excel formula searches for a value in the leftmost column of a '
                                              'table and returns a value in the same row?'},
                                     {   'answer': 'Pivot Table',
                                         'difficulty': 'Beginner',
                                         'options': ['Pivot Table', 'Data Validation', 'Goal Seek', 'Solver'],
                                         'q': 'What feature in Excel dynamically summarizes, groups, and '
                                              'cross-tabulates data without formula editing?'},
                                     {   'answer': 'INDEX and MATCH',
                                         'difficulty': 'Intermediate',
                                         'options': [   'INDEX and MATCH',
                                                        'VLOOKUP and HLOOKUP',
                                                        'SUMIF and COUNTIF',
                                                        'INDIRECT and OFFSET'],
                                         'q': 'Which formula combination provides a flexible dynamic lookup that '
                                              "doesn't require the lookup column to be leftmost?"},
                                     {   'answer': '=UNIQUE(FILTER(array, include_condition))',
                                         'difficulty': 'Advanced',
                                         'options': [   '=UNIQUE(FILTER(array, include_condition))',
                                                        '=DISTINCT(SUMIFS(array, condition))',
                                                        '=INDEX(MATCH(UNIQUE(array)))',
                                                        '=VLOOKUP_MULTI(array, condition)'],
                                         'q': 'Which dynamic array formula in modern Excel extracts unique items from '
                                              'a list filtered by specific criteria?'},
                                     {   'answer': 'INDIRECT is a volatile function forcing Excel to recalculate the '
                                                   'entire formula tree on every grid edit',
                                         'difficulty': 'Expert',
                                         'options': [   'INDIRECT is a volatile function forcing Excel to recalculate '
                                                        'the entire formula tree on every grid edit',
                                                        'INDIRECT cannot reference cells in other worksheets',
                                                        'INDIRECT limits sheet calculations to 256 rows',
                                                        'INDIRECT permanently overwrites cell raw values'],
                                         'q': 'In financial modeling, why is wrapping volatile function INDIRECT() '
                                              'inside thousands of grid cells detrimental?'}],
                        'Power BI': [   {   'answer': 'DAX',
                                            'difficulty': 'Basic',
                                            'options': ['M Code', 'DAX', 'SQL', 'VBA'],
                                            'q': 'What expression language is used in Power BI for custom calculated '
                                                 'columns, measures, and tables?'},
                                        {   'answer': 'Power Query Editor',
                                            'difficulty': 'Beginner',
                                            'options': [   'Power Query Editor',
                                                           'Power View',
                                                           'Power Pivot',
                                                           'Power Service'],
                                            'q': 'Which Power BI editor is utilized for data transformation, cleaning, '
                                                 'and unpivoting prior to loading data?'},
                                        {   'answer': 'Star Schema',
                                            'difficulty': 'Intermediate',
                                            'options': [   'Star Schema',
                                                           'Snowflake Schema with 10 normalization levels',
                                                           'Single monolithic flat table',
                                                           'Circular relation schema'],
                                            'q': 'In Power BI data modeling, what dimensional modeling schema is '
                                                 'industry standard for report speed?'},
                                        {   'answer': 'CALCULATE()',
                                            'difficulty': 'Advanced',
                                            'options': ['CALCULATE()', 'FILTER()', 'SUMX()', 'ALLSELECTED()'],
                                            'q': 'Which DAX function alters evaluation context by overriding existing '
                                                 'visual filters or applying new conditions?'},
                                        {   'answer': 'Remove unused high cardinality columns, split combined DateTime '
                                                      'columns into Date and Time keys, and replace calculated columns '
                                                      'with DAX measures',
                                            'difficulty': 'Expert',
                                            'options': [   'Remove unused high cardinality columns, split combined '
                                                           'DateTime columns into Date and Time keys, and replace '
                                                           'calculated columns with DAX measures',
                                                           'Enable Bidirectional Cross-filtering across all dimensions',
                                                           'Convert all DirectQuery tables to Import mode without '
                                                           'aggregations',
                                                           'Replace measures with M Query custom columns'],
                                            'q': 'How should you troubleshoot a high latency Power BI report caused by '
                                                 'high cardinality in Fact table columns?'}],
                        'Python': [   {   'answer': 'Pandas',
                                          'difficulty': 'Basic',
                                          'options': ['NumPy', 'Pandas', 'SciPy', 'Matplotlib'],
                                          'q': 'Which Python library is primarily used for tabular data manipulation '
                                               'and DataFrame operations?'},
                                      {   'answer': 'df.dropna()',
                                          'difficulty': 'Beginner',
                                          'options': ['df.dropna()', 'df.fillna()', 'df.remove_null()', 'df.clean()'],
                                          'q': 'Which Pandas method drops rows or columns with missing (NaN) values?'},
                                      {   'answer': 'pd.merge()',
                                          'difficulty': 'Intermediate',
                                          'options': ['pd.concat()', 'pd.merge()', 'pd.join_tables()', 'pd.append()'],
                                          'q': 'How do you merge two DataFrames on a common key column in Pandas?'},
                                      {   'answer': 'A Series with the original DataFrame index containing the '
                                                    'Category mean for each row',
                                          'difficulty': 'Advanced',
                                          'options': [   'An aggregated summary DataFrame grouped by Category',
                                                         'A Series with the original DataFrame index containing the '
                                                         'Category mean for each row',
                                                         'A modified DataFrame with rows filtered to above-average '
                                                         'sales',
                                                         'A dictionary of category mean values'],
                                          'q': "What does `df.groupby('Category')['Sales'].transform('mean')` return "
                                               'in Pandas?'},
                                      {   'answer': 'Use chunksize parameter in pd.read_csv() combined with dtype '
                                                    'downcasting',
                                          'difficulty': 'Expert',
                                          'options': [   'Use chunksize parameter in pd.read_csv() combined with dtype '
                                                         'downcasting',
                                                         'Increase Python recursion limit with sys.setrecursionlimit()',
                                                         'Read the entire file into a single string using '
                                                         'open().read()',
                                                         'Use df.apply() on raw unparsed text lines'],
                                          'q': 'When processing a 15GB CSV file on a memory-constrained 8GB RAM '
                                               'system, which approach optimizes Pandas memory consumption?'}],
                        'SQL': [   {   'answer': 'WHERE',
                                       'difficulty': 'Basic',
                                       'options': ['HAVING', 'WHERE', 'ORDER BY', 'GROUP FILTER'],
                                       'q': 'Which SQL clause filters records BEFORE any grouping or aggregation takes '
                                            'place?'},
                                   {   'answer': 'LEFT JOIN',
                                       'difficulty': 'Beginner',
                                       'options': ['INNER JOIN', 'RIGHT JOIN', 'LEFT JOIN', 'FULL OUTER JOIN'],
                                       'q': 'Which JOIN returns all records from the left table and matched records '
                                            'from the right table?'},
                                   {   'answer': 'AVG(amount) OVER (PARTITION BY category ORDER BY date ROWS BETWEEN '
                                                 'UNBOUNDED PRECEDING AND CURRENT ROW)',
                                       'difficulty': 'Intermediate',
                                       'options': [   'AVG(amount) OVER (PARTITION BY category ORDER BY date ROWS '
                                                      'BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)',
                                                      'SUM(amount) GROUP BY category ORDER BY date',
                                                      'CUMULATIVE_AVG(amount) BY category',
                                                      'ROW_NUMBER() OVER (ORDER BY date) * AVG(amount)'],
                                       'q': 'Which SQL window function computes a cumulative moving average across '
                                            'ordered rows?'},
                                   {   'answer': 'RANK() leaves gaps in sequence after ties, whereas DENSE_RANK() '
                                                 'assigns consecutive ranks without gaps',
                                       'difficulty': 'Advanced',
                                       'options': [   'RANK() leaves gaps in sequence after ties, whereas DENSE_RANK() '
                                                      'assigns consecutive ranks without gaps',
                                                      'DENSE_RANK() leaves gaps in sequence after ties, whereas RANK() '
                                                      'assigns consecutive ranks',
                                                      'RANK() works only on integer columns while DENSE_RANK() works '
                                                      'on string columns',
                                                      'There is no difference in ranking output'],
                                       'q': 'What is the key functional difference between RANK() and DENSE_RANK()?'},
                                   {   'answer': 'Convert correlated subqueries into CTEs/Window Functions and add '
                                                 'composite B-Tree indexes on join and filter columns',
                                       'difficulty': 'Expert',
                                       'options': [   'Convert correlated subqueries into CTEs/Window Functions and '
                                                      'add composite B-Tree indexes on join and filter columns',
                                                      'Replace INNER JOIN with CROSS JOIN and add OPTION (RECOMPILE)',
                                                      'Wrap query in a CURSOR loop fetching 1 row at a time',
                                                      'Cast all date filtering columns to VARCHAR format'],
                                       'q': 'When optimizing a slow analytical query featuring nested correlated '
                                            'subqueries on an unindexed 50M-row table, what query refactoring yields '
                                            'the greatest speedup?'}],
                        'Statistics': [   {   'answer': 'Median',
                                              'difficulty': 'Basic',
                                              'options': ['Mean', 'Median', 'Mode', 'Variance'],
                                              'q': 'What statistical measure represents the exact middle value of an '
                                                   'ordered dataset?'},
                                          {   'answer': 'Two-sample t-test',
                                              'difficulty': 'Beginner',
                                              'options': [   'Two-sample t-test',
                                                             'Chi-Square test',
                                                             'ANOVA',
                                                             'Pearson correlation'],
                                              'q': 'Which statistical hypothesis test compares the means of two '
                                                   'independent numerical samples?'},
                                          {   'answer': 'Reject null hypothesis; statistical evidence indicates '
                                                        'significant effect',
                                              'difficulty': 'Intermediate',
                                              'options': [   'Reject null hypothesis; statistical evidence indicates '
                                                             'significant effect',
                                                             'Accept null hypothesis; no significant difference',
                                                             'Sample size was insufficient',
                                                             'Type II error probability is 100%'],
                                              'q': 'What does a p-value less than alpha (p < 0.05) signify in a '
                                                   'hypothesis test?'},
                                          {   'answer': 'Central Limit Theorem',
                                              'difficulty': 'Advanced',
                                              'options': [   'Central Limit Theorem',
                                                             'Law of Large Numbers',
                                                             "Bayes' Theorem",
                                                             "Chebyshev's Inequality"],
                                              'q': 'What theorem states that the sample mean distribution approaches a '
                                                   'normal distribution as sample size grows?'},
                                          {   'answer': 'Remove or combine highly collinear predictors or use '
                                                        'Ridge/Lasso regularization',
                                              'difficulty': 'Expert',
                                              'options': [   'Remove or combine highly collinear predictors or use '
                                                             'Ridge/Lasso regularization',
                                                             'Log transform the dependent variable only',
                                                             'Switch to simple K-Means clustering',
                                                             'Increase significance threshold alpha to 0.50'],
                                              'q': 'In multiple linear regression, how do you handle severe '
                                                   'Multicollinearity (VIF > 10) between independent predictors?'}],
                        'Tableau': [   {   'answer': 'Dimension',
                                           'difficulty': 'Basic',
                                           'options': ['Dimension', 'Measure', 'Parameter', 'Set'],
                                           'q': 'What type of fields in Tableau hold discrete qualitative attributes '
                                                'like Region or Customer Name?'},
                                       {   'answer': 'Green',
                                           'difficulty': 'Beginner',
                                           'options': ['Green', 'Blue', 'Red', 'Yellow'],
                                           'q': 'What color visual cue represents continuous fields in Tableau '
                                                'worksheet pills?'},
                                       {   'answer': 'Level of Detail (LOD) Expression',
                                           'difficulty': 'Intermediate',
                                           'options': [   'Level of Detail (LOD) Expression',
                                                          'Table Calculation',
                                                          'Quick Table Calculation',
                                                          'Row-level expression'],
                                           'q': 'Which calculation type in Tableau evaluates at a specific level of '
                                                'detail independent of view dimensions?'},
                                       {   'answer': '{FIXED} evaluates using only specified dimensions ignoring view '
                                                     'dimensions, whereas {INCLUDE} adds specified dimensions to view '
                                                     'dimensions',
                                           'difficulty': 'Advanced',
                                           'options': [   '{FIXED} evaluates using only specified dimensions ignoring '
                                                          'view dimensions, whereas {INCLUDE} adds specified '
                                                          'dimensions to view dimensions',
                                                          '{FIXED} respects view filters while {INCLUDE} ignores all '
                                                          'filters',
                                                          '{FIXED} only works on measures, {INCLUDE} only on '
                                                          'dimensions',
                                                          'Both function identically in filter pipeline'],
                                           'q': 'What distinguishes {FIXED} LOD expressions from {INCLUDE} LOD '
                                                'expressions regarding view context?'},
                                       {   'answer': 'Create aggregated extracts, replace Quick Filters with Action '
                                                     'Filters, and index database join columns',
                                           'difficulty': 'Expert',
                                           'options': [   'Create aggregated extracts, replace Quick Filters with '
                                                          'Action Filters, and index database join columns',
                                                          'Add floating text boxes and nested table calculations',
                                                          'Convert discrete dimensions into continuous green pills',
                                                          'Disable extract refreshes and compute row-level logic on '
                                                          'client side'],
                                           'q': 'When optimizing a enterprise Tableau dashboard linked to live '
                                                'multi-million row database tables, which strategy yields maximum '
                                                'rendering performance?'}]},
    'Full Stack Developer': {   'CSS': [   {   'answer': 'color',
                                               'difficulty': 'Basic',
                                               'options': ['color', 'text-color', 'font-color', 'background-color'],
                                               'q': 'Which CSS property changes the text color of an HTML element?'},
                                           {   'answer': 'Flexbox',
                                               'difficulty': 'Beginner',
                                               'options': ['Flexbox', 'CSS Grid', 'Float', 'Table'],
                                               'q': 'Which CSS layout module provides one-dimensional alignment for '
                                                    'rows or columns?'},
                                           {   'answer': 'Inline styles (1000) > IDs (100) > '
                                                         'Classes/Attributes/Pseudo-classes (10) > '
                                                         'Elements/Pseudo-elements (1)',
                                               'difficulty': 'Intermediate',
                                               'options': [   'Inline styles (1000) > IDs (100) > '
                                                              'Classes/Attributes/Pseudo-classes (10) > '
                                                              'Elements/Pseudo-elements (1)',
                                                              'Elements (100) > Classes (10) > IDs (1)',
                                                              'Order of definition in CSS file is the only rule',
                                                              'Alphabetical order of class names'],
                                               'q': 'How does CSS Specificity calculate precedence between selectors?'},
                                           {   'answer': '@media query',
                                               'difficulty': 'Advanced',
                                               'options': ['@media query', '@container query', '@import', '@supports'],
                                               'q': 'What CSS rule creates responsive layouts based on device viewport '
                                                    'dimensions or features?'},
                                           {   'answer': 'They offload element rendering onto GPU composite layers, '
                                                         'avoiding expensive Reflow (Layout) and Repaint cycles on the '
                                                         'CPU main thread',
                                               'difficulty': 'Expert',
                                               'options': [   'They offload element rendering onto GPU composite '
                                                              'layers, avoiding expensive Reflow (Layout) and Repaint '
                                                              'cycles on the CPU main thread',
                                                              'They disable CSS Box Model calculations permanently',
                                                              'They force synchronous DOM recalculations before '
                                                              'repaint',
                                                              'They convert vector animations into animated GIF '
                                                              'images'],
                                               'q': 'How do browser hardware acceleration and `will-change: transform` '
                                                    'prevent layout thrashing during animations?'}],
                                'Django': [   {   'answer': 'models.py',
                                                  'difficulty': 'Basic',
                                                  'options': ['models.py', 'views.py', 'urls.py', 'admin.py'],
                                                  'q': 'Which Django file defines data models and database fields?'},
                                              {   'answer': 'python manage.py migrate',
                                                  'difficulty': 'Beginner',
                                                  'options': [   'python manage.py migrate',
                                                                 'python manage.py makemigrations',
                                                                 'python manage.py runserver',
                                                                 'python manage.py collectstatic'],
                                                  'q': 'Which Django command applies pending migrations to update the '
                                                       'database schema?'},
                                              {   'answer': 'django.contrib.auth',
                                                  'difficulty': 'Intermediate',
                                                  'options': [   'django.contrib.auth',
                                                                 'django.contrib.admin',
                                                                 'django.contrib.sessions',
                                                                 'django.contrib.messages'],
                                                  'q': 'What tool in Django handles user authentication, groups, '
                                                       'permissions, and password hashing out of the box?'},
                                              {   'answer': 'They wrap request processing in a chain of callable '
                                                            'methods (`process_request`, `process_response`) executed '
                                                            'in order before and after view execution',
                                                  'difficulty': 'Advanced',
                                                  'options': [   'They wrap request processing in a chain of callable '
                                                                 'methods (`process_request`, `process_response`) '
                                                                 'executed in order before and after view execution',
                                                                 'They replace models.py database definitions',
                                                                 'They compile HTML templates into JavaScript bytecode',
                                                                 'They run as external background processes on '
                                                                 'separate servers'],
                                                  'q': 'How do custom Django Middleware classes process requests and '
                                                       'responses?'},
                                              {   'answer': 'Store short-lived access tokens in memory and long-lived '
                                                            'refresh tokens in httpOnly, Secure, SameSite cookies',
                                                  'difficulty': 'Expert',
                                                  'options': [   'Store short-lived access tokens in memory and '
                                                                 'long-lived refresh tokens in httpOnly, Secure, '
                                                                 'SameSite cookies',
                                                                 'Store refresh tokens in localStorage as plaintext '
                                                                 'strings',
                                                                 'Include database user passwords inside JWT headers',
                                                                 'Disable token expiration entirely'],
                                                  'q': 'When deploying Django REST Framework (DRF) alongside React '
                                                       'frontends, how should token refreshing be securely managed?'}],
                                'HTML': [   {   'answer': '<nav>',
                                                'difficulty': 'Basic',
                                                'options': ['<nav>', '<header>', '<section>', '<aside>'],
                                                'q': 'Which HTML5 semantic element is used to define navigation '
                                                     'links?'},
                                            {   'answer': 'alt',
                                                'difficulty': 'Beginner',
                                                'options': ['alt', 'title', 'src', 'description'],
                                                'q': 'Which HTML attribute specifies alternative text for an image if '
                                                     'it cannot be displayed?'},
                                            {   'answer': 'To enhance accessibility for assistive technologies like '
                                                          'screen readers',
                                                'difficulty': 'Intermediate',
                                                'options': [   'To enhance accessibility for assistive technologies '
                                                               'like screen readers',
                                                               'To apply CSS styles dynamically without stylesheets',
                                                               'To speed up HTML parsing in modern browser engines',
                                                               'To validate form inputs on server side'],
                                                'q': 'What is the primary function of WAI-ARIA attributes (e.g., '
                                                     '`role`, `aria-label`) in HTML5?'},
                                            {   'answer': 'The script downloads asynchronously in parallel with HTML '
                                                          'parsing and executes after HTML DOM construction completes',
                                                'difficulty': 'Advanced',
                                                'options': [   'The script downloads asynchronously in parallel with '
                                                               'HTML parsing and executes after HTML DOM construction '
                                                               'completes',
                                                               'The script executes immediately, blocking DOM parsing',
                                                               'The script only executes when triggered by inline '
                                                               'onclick events',
                                                               'The script is skipped entirely unless manually called'],
                                                'q': 'What happens when `<script defer>` is placed in the HTML '
                                                     '`<head>` section?'},
                                            {   'answer': 'It isolates DOM subtree elements and CSS styles so outer '
                                                          'document styles and scripts cannot leak in or affect '
                                                          'internal component structure',
                                                'difficulty': 'Expert',
                                                'options': [   'It isolates DOM subtree elements and CSS styles so '
                                                               'outer document styles and scripts cannot leak in or '
                                                               'affect internal component structure',
                                                               'It hides HTML source code from browser developer tools',
                                                               'It encrypts DOM nodes before sending to server',
                                                               'It automatically converts HTML tags into canvas '
                                                               'graphics'],
                                                'q': 'How does Shadow DOM encapsulation protect Web Components in HTML '
                                                     'modern applications?'}],
                                'JavaScript': [   {   'answer': 'let',
                                                      'difficulty': 'Basic',
                                                      'options': ['let', 'var', 'global', 'define'],
                                                      'q': 'Which keyword declares a block-scoped variable in '
                                                           'JavaScript that cannot be re-declared in the same scope?'},
                                                  {   'answer': "'object'",
                                                      'difficulty': 'Beginner',
                                                      'options': ["'object'", "'null'", "'undefined'", "'boolean'"],
                                                      'q': 'What is the result of `typeof null` in JavaScript?'},
                                                  {   'answer': 'Closure',
                                                      'difficulty': 'Intermediate',
                                                      'options': ['Closure', 'Hoisting', 'Callback', 'Prototype Chain'],
                                                      'q': 'What feature allows inner functions to access variables '
                                                           'from their enclosing lexical scope even after parent '
                                                           'function execution completes?'},
                                                  {   'answer': 'The Microtask queue (Promises, queueMicrotask) is '
                                                                'completely drained after every task before processing '
                                                                'the next Macrotask (setTimeout, setInterval)',
                                                      'difficulty': 'Advanced',
                                                      'options': [   'The Microtask queue (Promises, queueMicrotask) '
                                                                     'is completely drained after every task before '
                                                                     'processing the next Macrotask (setTimeout, '
                                                                     'setInterval)',
                                                                     'Macrotasks are executed with higher priority '
                                                                     'than Microtasks',
                                                                     'Microtasks and Macrotasks run in parallel '
                                                                     'threads on multi-core CPUs',
                                                                     'The Event Loop randomly picks tasks from both '
                                                                     'queues'],
                                                      'q': 'How does the JavaScript Event Loop coordinate execution '
                                                           'between Microtasks and Macrotasks?'},
                                                  {   'answer': 'Remove event listeners explicitly on component '
                                                                'unmount and use `WeakMap` or `WeakSet` for object '
                                                                'references',
                                                      'difficulty': 'Expert',
                                                      'options': [   'Remove event listeners explicitly on component '
                                                                     'unmount and use `WeakMap` or `WeakSet` for '
                                                                     'object references',
                                                                     'Set all variables to global `window` scope',
                                                                     'Use `eval()` inside interval timers',
                                                                     'Disable browser garbage collection using '
                                                                     '`console.clear()`'],
                                                      'q': 'How can you prevent memory leaks caused by detached DOM '
                                                           'nodes and uncleared event listeners in single-page '
                                                           'JavaScript web apps?'}],
                                'Python': [   {   'answer': 'def',
                                                  'difficulty': 'Basic',
                                                  'options': ['def', 'function', 'func', 'define'],
                                                  'q': 'Which keyword defines a function in Python?'},
                                              {   'answer': '2',
                                                  'difficulty': 'Beginner',
                                                  'options': ['2', '4', '1', 'Error'],
                                                  'q': "What is the result of `len({'a': 1, 'b': 2})`?"},
                                              {   'answer': 'enumerate()',
                                                  'difficulty': 'Intermediate',
                                                  'options': ['enumerate()', 'zip()', 'map()', 'filter()'],
                                                  'q': 'Which built-in Python function turns an iterable into pairs of '
                                                       '`(index, element)`?'},
                                              {   'answer': 'Shallow copy constructs a new object inserting references '
                                                            'to child objects; deep copy recursively copies child '
                                                            'objects',
                                                  'difficulty': 'Advanced',
                                                  'options': [   'Shallow copy constructs a new object inserting '
                                                                 'references to child objects; deep copy recursively '
                                                                 'copies child objects',
                                                                 'Deep copy copies references only; shallow copy '
                                                                 'copies recursively',
                                                                 'Shallow copy converts objects to JSON strings',
                                                                 'Deep copy works only on primitive numeric data '
                                                                 'types'],
                                                  'q': 'What is the key difference between deep copy and shallow copy '
                                                       "in Python's `copy` module?"},
                                              {   'answer': 'They execute `__enter__()` before block entry and '
                                                            'guarantee `__exit__()` execution upon block exit even if '
                                                            'exceptions are raised',
                                                  'difficulty': 'Expert',
                                                  'options': [   'They execute `__enter__()` before block entry and '
                                                                 'guarantee `__exit__()` execution upon block exit '
                                                                 'even if exceptions are raised',
                                                                 'They run `__init__()` and `__del__()` asynchronously '
                                                                 'on a background thread',
                                                                 'They wrap functions in `try...except` blocks '
                                                                 'automatically',
                                                                 'They disable garbage collection while inside the '
                                                                 'context block'],
                                                  'q': 'How do context managers (`with` statement) implement resource '
                                                       'allocation and cleanup using magic methods in Python?'}],
                                'REST API': [   {   'answer': 'Content-Type',
                                                    'difficulty': 'Basic',
                                                    'options': [   'Content-Type',
                                                                   'Accept',
                                                                   'Authorization',
                                                                   'User-Agent'],
                                                    'q': 'Which HTTP header specifies the format of the data being '
                                                         'sent in a request body (e.g. `application/json`)?'},
                                                {   'answer': 'The client is authenticated but lacks required '
                                                              'permission to access the resource',
                                                    'difficulty': 'Beginner',
                                                    'options': [   'The client is authenticated but lacks required '
                                                                   'permission to access the resource',
                                                                   'The requested resource was not found on the server',
                                                                   'The request payload format was invalid JSON',
                                                                   'The server encountered an unhandled exception'],
                                                    'q': 'What does HTTP status code 403 Forbidden indicate?'},
                                                {   'answer': 'CORS (Cross-Origin Resource Sharing)',
                                                    'difficulty': 'Intermediate',
                                                    'options': [   'CORS (Cross-Origin Resource Sharing)',
                                                                   'CSRF Token',
                                                                   'Content Security Policy (CSP)',
                                                                   'SSL Pinning'],
                                                    'q': 'What mechanism allows servers to specify which external '
                                                         'origin domains can fetch resources via cross-site browser '
                                                         'requests?'},
                                                {   'answer': 'A method where making multiple identical requests '
                                                              'yields the exact same server state result as a single '
                                                              'request (e.g., PUT, DELETE, GET)',
                                                    'difficulty': 'Advanced',
                                                    'options': [   'A method where making multiple identical requests '
                                                                   'yields the exact same server state result as a '
                                                                   'single request (e.g., PUT, DELETE, GET)',
                                                                   'A method that can only be called once per IP '
                                                                   'address',
                                                                   'A method that returns encrypted responses',
                                                                   'A method that requires WebSocket connections'],
                                                    'q': "In REST API design, what is an 'Idempotent' method?"},
                                                {   'answer': 'They inspect incoming JWT tokens at the gateway '
                                                              'boundary, reject invalid requests early, and rate-limit '
                                                              'IP/Key buckets before proxying to backend services',
                                                    'difficulty': 'Expert',
                                                    'options': [   'They inspect incoming JWT tokens at the gateway '
                                                                   'boundary, reject invalid requests early, and '
                                                                   'rate-limit IP/Key buckets before proxying to '
                                                                   'backend services',
                                                                   'They pass all unvalidated traffic directly to '
                                                                   'microservices to evaluate auth',
                                                                   'They convert incoming REST HTTP calls into SQL '
                                                                   'queries directly',
                                                                   'They store user session states in browser cookies'],
                                                    'q': 'How do API Gateways handle Authentication Offloading and '
                                                         'Microservice Rate Limiting?'}],
                                'React.js': [   {   'answer': 'useState',
                                                    'difficulty': 'Basic',
                                                    'options': ['useState', 'useEffect', 'useContext', 'useRef'],
                                                    'q': 'Which React Hook manages state inside functional '
                                                         'components?'},
                                                {   'answer': 'JSX',
                                                    'difficulty': 'Beginner',
                                                    'options': ['JSX', 'TSX', 'HTML5', 'ECMAScript Template'],
                                                    'q': 'What syntax extension allows writing HTML-like markup inside '
                                                         'JavaScript React components?'},
                                                {   'answer': 'useEffect',
                                                    'difficulty': 'Intermediate',
                                                    'options': ['useEffect', 'useState', 'useMemo', 'useCallback'],
                                                    'q': 'Which Hook performs side effects (fetching data, subscribing '
                                                         'to timers) in functional React components?'},
                                                {   'answer': 'It gives React a stable identity for items so Virtual '
                                                              'DOM diffing can accurately reorder, insert, or remove '
                                                              'nodes without re-rendering unchanged children',
                                                    'difficulty': 'Advanced',
                                                    'options': [   'It gives React a stable identity for items so '
                                                                   'Virtual DOM diffing can accurately reorder, '
                                                                   'insert, or remove nodes without re-rendering '
                                                                   'unchanged children',
                                                                   'It applies CSS styling to list items',
                                                                   'It encrypts list element state',
                                                                   'It binds event handlers to list items '
                                                                   'automatically'],
                                                    'q': 'Why is passing `key` props crucial when rendering dynamic '
                                                         'arrays of components in React?'},
                                                {   'answer': 'useMemo memoizes calculated values, and useCallback '
                                                              'memoizes function instances across re-renders when '
                                                              "dependencies haven't changed",
                                                    'difficulty': 'Expert',
                                                    'options': [   'useMemo memoizes calculated values, and '
                                                                   'useCallback memoizes function instances across '
                                                                   "re-renders when dependencies haven't changed",
                                                                   'useMemo modifies DOM elements directly skipping '
                                                                   'React Virtual DOM',
                                                                   'useCallback forces immediate synchronous component '
                                                                   'mounts',
                                                                   'Both hooks convert functional components into '
                                                                   'class components automatically'],
                                                    'q': 'How do `useMemo` and `useCallback` prevent unnecessary '
                                                         'component re-renders in large React render trees?'}],
                                'SQL': [   {   'answer': 'DROP TABLE',
                                               'difficulty': 'Basic',
                                               'options': [   'DROP TABLE',
                                                              'DELETE FROM',
                                                              'TRUNCATE TABLE',
                                                              'REMOVE TABLE'],
                                               'q': 'Which SQL statement is used to remove a table structure and all '
                                                    'its data permanently from a database?'},
                                           {   'answer': 'Groups rows sharing identical column values into summary '
                                                         'rows',
                                               'difficulty': 'Beginner',
                                               'options': [   'Groups rows sharing identical column values into '
                                                              'summary rows',
                                                              'Sorts query output alphabetically',
                                                              'Joins two foreign tables on a primary key',
                                                              'Enforces unique constraints on columns'],
                                               'q': 'What does the `GROUP BY` clause do in a SQL query?'},
                                           {   'answer': 'PRIMARY KEY',
                                               'difficulty': 'Intermediate',
                                               'options': ['PRIMARY KEY', 'FOREIGN KEY', 'CHECK', 'DEFAULT'],
                                               'q': 'What SQL constraint ensures that all values in a column are '
                                                    'unique and non-null?'},
                                           {   'answer': 'Eliminate data redundancy and prevent update/insertion '
                                                         'anomalies by organizing fields into logical normalized '
                                                         'tables',
                                               'difficulty': 'Advanced',
                                               'options': [   'Eliminate data redundancy and prevent update/insertion '
                                                              'anomalies by organizing fields into logical normalized '
                                                              'tables',
                                                              'Increase query response time by duplicating data across '
                                                              'tables',
                                                              'Encrypt sensitive customer fields automatically',
                                                              'Convert relational tables into NoSQL JSON documents'],
                                               'q': 'What is database Normalization (1NF, 2NF, 3NF) designed to '
                                                    'achieve?'},
                                           {   'answer': 'Index Seek navigates B-Tree nodes directly for specific keys '
                                                         '(O(log N)), while Index Scan traverses the entire index leaf '
                                                         'chain (O(N))',
                                               'difficulty': 'Expert',
                                               'options': [   'Index Seek navigates B-Tree nodes directly for specific '
                                                              'keys (O(log N)), while Index Scan traverses the entire '
                                                              'index leaf chain (O(N))',
                                                              'Index Scan is always faster than Index Seek',
                                                              'Index Seek is used only for text wildcard searches',
                                                              'Index Scan requires full table locks on write '
                                                              'operations'],
                                               'q': 'How does SQL Query Optimizer use Index Scans vs Index Seeks when '
                                                    'executing filtering queries?'}]},
    'Python Developer': {   'DSA using Python': [   {   'answer': 'O(log n)',
                                                        'difficulty': 'Basic',
                                                        'options': ['O(1)', 'O(log n)', 'O(n)', 'O(n log n)'],
                                                        'q': 'What is the average time complexity of searching an '
                                                             'element in a balanced Binary Search Tree (BST)?'},
                                                    {   'answer': 'Stack',
                                                        'difficulty': 'Beginner',
                                                        'options': ['Queue', 'Stack', 'Linked List', 'Tree'],
                                                        'q': 'Which data structure operates on a Last-In, First-Out '
                                                             '(LIFO) principle?'},
                                                    {   'answer': "Dijkstra's Algorithm",
                                                        'difficulty': 'Intermediate',
                                                        'options': [   "Dijkstra's Algorithm",
                                                                       'Breadth-First Search (BFS)',
                                                                       'Depth-First Search (DFS)',
                                                                       "Kruskal's Algorithm"],
                                                        'q': 'Which algorithm finds the shortest path from a single '
                                                             'source vertex to all other vertices in a weighted graph '
                                                             'with non-negative edge weights?'},
                                                    {   'answer': 'By combining a Hash Map (dict) with a Doubly Linked '
                                                                  'List',
                                                        'difficulty': 'Advanced',
                                                        'options': [   'By combining a Hash Map (dict) with a Doubly '
                                                                       'Linked List',
                                                                       'By using a Min-Heap combined with a Binary '
                                                                       'Search Tree',
                                                                       'By sorting an array after every insertion',
                                                                       'By using recursive Memoization with Python '
                                                                       'set'],
                                                        'q': 'How does LRU (Least Recently Used) Cache achieve O(1) '
                                                             'time complexity for both `get` and `put` operations in '
                                                             'Python?'},
                                                    {   'answer': 'It avoids redundant subproblem calculations by '
                                                                  'storing intermediate results, reducing time '
                                                                  'complexity from exponential O(2^n) to '
                                                                  'pseudo-polynomial O(n*W)',
                                                        'difficulty': 'Expert',
                                                        'options': [   'It avoids redundant subproblem calculations by '
                                                                       'storing intermediate results, reducing time '
                                                                       'complexity from exponential O(2^n) to '
                                                                       'pseudo-polynomial O(n*W)',
                                                                       'It reduces spatial complexity to O(1) '
                                                                       'guaranteed',
                                                                       'It converts non-linear constraints into linear '
                                                                       'equations',
                                                                       'It eliminates greedy search failure modes'],
                                                        'q': 'When solving the 0/1 Knapsack Problem dynamically, why '
                                                             'is top-down memoization preferred over naive '
                                                             'recursion?'}],
                            'Django': [   {   'answer': 'python manage.py makemigrations',
                                              'difficulty': 'Basic',
                                              'options': [   'python manage.py makemigrations',
                                                             'python manage.py migrate',
                                                             'python manage.py syncdb',
                                                             'python manage.py buildmodels'],
                                              'q': 'Which command creates database schema migration files based on '
                                                   'changes detected in `models.py`?'},
                                          {   'answer': 'MVT (Model-View-Template)',
                                              'difficulty': 'Beginner',
                                              'options': [   'MVT (Model-View-Template)',
                                                             'MVC (Model-View-Controller)',
                                                             'MVVM (Model-View-ViewModel)',
                                                             'Flux Architecture'],
                                              'q': 'Which pattern architecture does Django natively follow?'},
                                          {   'answer': 'Use `select_related()` for single foreign keys and '
                                                        '`prefetch_related()` for many-to-many/many-to-one relations',
                                              'difficulty': 'Intermediate',
                                              'options': [   'Use `select_related()` for single foreign keys and '
                                                             '`prefetch_related()` for many-to-many/many-to-one '
                                                             'relations',
                                                             'Loop over QuerySet manually using `values_list()`',
                                                             'Set `db_index=True` on every model field',
                                                             'Disable Django ORM caching'],
                                              'q': 'How do you prevent the N+1 query problem when fetching related '
                                                   'foreign key objects in Django ORM?'},
                                          {   'answer': 'It injects a secret cryptographically signed token into user '
                                                        'sessions and verifies matching token header in POST requests',
                                              'difficulty': 'Advanced',
                                              'options': [   'It injects a secret cryptographically signed token into '
                                                             'user sessions and verifies matching token header in POST '
                                                             'requests',
                                                             'It blocks requests coming from external IP addresses',
                                                             'It encrypts database passwords before session storage',
                                                             'It limits request rate to 10 requests per minute'],
                                              'q': "How does Django's built-in CSRF middleware protect forms against "
                                                   'Cross-Site Request Forgery?'},
                                          {   'answer': 'Celery with Redis/RabbitMQ message broker combined with '
                                                        'Django Channels for WebSocket push notifications',
                                              'difficulty': 'Expert',
                                              'options': [   'Celery with Redis/RabbitMQ message broker combined with '
                                                             'Django Channels for WebSocket push notifications',
                                                             'Synchronous threads inside `views.py` using '
                                                             '`threading.Thread`',
                                                             'Database triggers executing raw SQL stored procedures',
                                                             'Custom infinite while loops inside Django middleware'],
                                              'q': 'When scaling a multi-tenant Django application with asynchronous '
                                                   'long-running background tasks, what infrastructure stack is best '
                                                   'suited?'}],
                            'Flask': [   {   'answer': '@app.route()',
                                             'difficulty': 'Basic',
                                             'options': ['@app.route()', '@app.bind()', '@app.path()', '@app.url()'],
                                             'q': 'Which decorator in Flask binds a view function to an HTTP URL '
                                                  'path?'},
                                         {   'answer': 'request.get_json()',
                                             'difficulty': 'Beginner',
                                             'options': [   'request.get_json()',
                                                            'request.form[]',
                                                            'request.args.get()',
                                                            'request.body'],
                                             'q': 'How do you retrieve JSON payload data sent in a POST request within '
                                                  'a Flask view function?'},
                                         {   'answer': 'Blueprints',
                                             'difficulty': 'Intermediate',
                                             'options': ['Blueprints', 'Modules', 'Routes', 'Templates'],
                                             'q': 'What feature in Flask allows modular structuring of large '
                                                  'applications into smaller logical components?'},
                                         {   'answer': 'LocalProxy object (`request`, `g`) tied to current '
                                                       'thread/async task context',
                                             'difficulty': 'Advanced',
                                             'options': [   'LocalProxy object (`request`, `g`) tied to current '
                                                            'thread/async task context',
                                                            'Global static dictionary `flask.globals`',
                                                            'Database ORM session wrapper',
                                                            'WSGI application environment object'],
                                             'q': 'In Flask, what object proxy allows accessing thread-safe request '
                                                  'context data without passing request parameters explicitly?'},
                                         {   'answer': 'Gunicorn / uWSGI behind Nginx reverse proxy with gevent or '
                                                       'async worker class',
                                             'difficulty': 'Expert',
                                             'options': [   'Gunicorn / uWSGI behind Nginx reverse proxy with gevent '
                                                            'or async worker class',
                                                            "Run built-in `app.run(debug=True, host='0.0.0.0')` "
                                                            'development server',
                                                            'Wrap Flask inside single-threaded CGI script executed by '
                                                            'Apache',
                                                            'Execute Flask view functions directly via cron jobs'],
                                             'q': 'When deploying a production Flask app handling 10,000 concurrent '
                                                  'requests, what web server deployment architecture is recommended?'}],
                            'OOPs using Python': [   {   'answer': 'Inheritance',
                                                         'difficulty': 'Basic',
                                                         'options': [   'Encapsulation',
                                                                        'Inheritance',
                                                                        'Polymorphism',
                                                                        'Abstraction'],
                                                         'q': 'Which Object-Oriented principle allows a child class to '
                                                              'inherit attributes and methods from a parent class?'},
                                                     {   'answer': '__init__',
                                                         'difficulty': 'Beginner',
                                                         'options': ['__new__', '__init__', '__str__', '__call__'],
                                                         'q': 'Which magic method in Python initializes newly created '
                                                              'object instances?'},
                                                     {   'answer': '@property',
                                                         'difficulty': 'Intermediate',
                                                         'options': [   '@staticmethod',
                                                                        '@classmethod',
                                                                        '@property',
                                                                        '@abstractmethod'],
                                                         'q': 'What decorator creates a read-only getter attribute in '
                                                              'a Python class?'},
                                                     {   'answer': 'It follows the C3 Linearization algorithm to '
                                                                   'determine a deterministic order of base classes',
                                                         'difficulty': 'Advanced',
                                                         'options': [   'It follows the C3 Linearization algorithm to '
                                                                        'determine a deterministic order of base '
                                                                        'classes',
                                                                        'It checks base classes in random order at '
                                                                        'runtime',
                                                                        'It always prioritizes the last defined parent '
                                                                        'class',
                                                                        'It raises an AmbiguityError whenever two '
                                                                        'parents define the same method'],
                                                         'q': 'In Python multiple inheritance, how does the Method '
                                                              'Resolution Order (MRO) resolve method calls using '
                                                              '`super()`?'},
                                                     {   'answer': 'High-level modules should not depend on low-level '
                                                                   'concrete classes; both should depend on '
                                                                   'abstractions (interfaces or Abstract Base Classes)',
                                                         'difficulty': 'Expert',
                                                         'options': [   'High-level modules should not depend on '
                                                                        'low-level concrete classes; both should '
                                                                        'depend on abstractions (interfaces or '
                                                                        'Abstract Base Classes)',
                                                                        'Classes should be open for modification and '
                                                                        'closed for extension',
                                                                        'Objects should be initialized using singleton '
                                                                        'magic methods only',
                                                                        'Subclasses must throw errors if they modify '
                                                                        'inherited methods'],
                                                         'q': "How does the SOLID 'Dependency Inversion Principle' "
                                                              'apply to Python backend class architectures?'}],
                            'Python': [   {   'answer': 'yield',
                                              'difficulty': 'Basic',
                                              'options': ['return', 'yield', 'generate', 'emit'],
                                              'q': 'Which Python keyword is used to return a generator from a function '
                                                   'instead of a single value?'},
                                          {   'answer': 'False',
                                              'difficulty': 'Beginner',
                                              'options': ['True', 'False', 'None', 'Error'],
                                              'q': 'What is the output of `bool([])` in Python?'},
                                          {   'answer': 'asyncio',
                                              'difficulty': 'Intermediate',
                                              'options': [   'threading',
                                                             'multiprocessing',
                                                             'asyncio',
                                                             'concurrent.futures'],
                                              'q': 'Which standard library module handles asynchronous concurrent I/O '
                                                   'loops using async and await syntax?'},
                                          {   'answer': 'The GIL prevents multiple native OS threads from executing '
                                                        'Python bytecodes in parallel on multiple CPU cores',
                                              'difficulty': 'Advanced',
                                              'options': [   'The GIL prevents multiple native OS threads from '
                                                             'executing Python bytecodes in parallel on multiple CPU '
                                                             'cores',
                                                             'The GIL speeds up CPU-bound tasks by auto-vectorizing '
                                                             'loops',
                                                             'The GIL restricts file read operations to a single '
                                                             'thread',
                                                             'The GIL disables memory garbage collection during loop '
                                                             'execution'],
                                              'q': 'In Python, how does the Global Interpreter Lock (GIL) affect '
                                                   'multithreaded CPU-bound execution?'},
                                          {   'answer': 'Define `__slots__` inside the class definition specifying '
                                                        'attribute names as a tuple',
                                              'difficulty': 'Expert',
                                              'options': [   'Define `__slots__` inside the class definition '
                                                             'specifying attribute names as a tuple',
                                                             'Decorate the class with `@classmethod` and '
                                                             '`@staticmethod`',
                                                             'Inherit from `collections.defaultdict`',
                                                             'Override the `__getattr__` and `__setattr__` magic '
                                                             'methods to raise AttributeError'],
                                              'q': 'How can you implement a memory-efficient custom object with locked '
                                                   'attribute keys in Python to reduce per-instance dict overhead?'}],
                            'REST API': [   {   'answer': 'PUT',
                                                'difficulty': 'Basic',
                                                'options': ['POST', 'PUT', 'GET', 'DELETE'],
                                                'q': 'Which HTTP method is idempotent and primarily used to update an '
                                                     'existing resource completely?'},
                                            {   'answer': '201 Created',
                                                'difficulty': 'Beginner',
                                                'options': [   '200 OK',
                                                               '201 Created',
                                                               '400 Bad Request',
                                                               '404 Not Found'],
                                                'q': 'What HTTP response status code represents a successful resource '
                                                     "creation ('Created')?"},
                                            {   'answer': 'JWT (JSON Web Token)',
                                                'difficulty': 'Intermediate',
                                                'options': [   'JWT (JSON Web Token)',
                                                               'Basic Auth',
                                                               'API Key in query string',
                                                               'Cookies only'],
                                                'q': 'What token authentication standard stores cryptographically '
                                                     'signed JSON payloads sent in HTTP Authorization headers?'},
                                            {   'answer': 'API Versioning via URL paths (e.g., /api/v1/resource vs '
                                                          '/api/v2/resource) or custom Accept headers',
                                                'difficulty': 'Advanced',
                                                'options': [   'API Versioning via URL paths (e.g., /api/v1/resource '
                                                               'vs /api/v2/resource) or custom Accept headers',
                                                               'Modifying existing JSON keys directly in production',
                                                               'Returning HTTP 500 error code on legacy requests',
                                                               'Overwriting old endpoints with GraphQL schemas without '
                                                               'notice'],
                                                'q': 'What design strategy guarantees API backward compatibility when '
                                                     'breaking endpoint schema changes are introduced?'},
                                            {   'answer': 'Implement Rate Limiting using Token Bucket / Leaky Bucket '
                                                          'algorithms via API Gateway (e.g., Kong/Nginx) combined with '
                                                          'OAuth2 scope validation',
                                                'difficulty': 'Expert',
                                                'options': [   'Implement Rate Limiting using Token Bucket / Leaky '
                                                               'Bucket algorithms via API Gateway (e.g., Kong/Nginx) '
                                                               'combined with OAuth2 scope validation',
                                                               'Disable HTTP caching headers on all endpoints',
                                                               'Allow infinite CORS origins across all endpoints',
                                                               'Enforce synchronous database locking on every GET '
                                                               'request'],
                                                'q': 'How do you defend a public microservices REST API against Denial '
                                                     'of Service (DoS) and brute-force key attacks?'}],
                            'SQL': [   {   'answer': 'INSERT INTO',
                                           'difficulty': 'Basic',
                                           'options': ['INSERT INTO', 'UPDATE', 'ADD ROW', 'APPEND'],
                                           'q': 'Which SQL statement adds new data rows to an existing table?'},
                                       {   'answer': 'To speed up data retrieval queries at the cost of additional '
                                                     'write overhead',
                                           'difficulty': 'Beginner',
                                           'options': [   'To speed up data retrieval queries at the cost of '
                                                          'additional write overhead',
                                                          'To encrypt column values for security',
                                                          'To format text strings into uppercase',
                                                          'To automatically delete duplicate rows'],
                                           'q': 'What is the purpose of an INDEX on a SQL database column?'},
                                       {   'answer': 'COMMIT',
                                           'difficulty': 'Intermediate',
                                           'options': ['COMMIT', 'ROLLBACK', 'SAVEPOINT', 'CHECKPOINT'],
                                           'q': 'What SQL clause handles transactional atomic operations by persisting '
                                                'changes to disk?'},
                                       {   'answer': 'Phantom Reads',
                                           'difficulty': 'Advanced',
                                           'options': [   'Phantom Reads',
                                                          'Dirty Reads',
                                                          'Non-Repeatable Reads',
                                                          'Lost Updates'],
                                           'q': 'In SQL database isolation levels, what concurrency anomaly does '
                                                '`SERIALIZABLE` isolation prevent that `REPEATABLE READ` allows?'},
                                       {   'answer': 'Access tables and rows in a consistent deterministic order '
                                                     'across transactions and keep transactions short',
                                           'difficulty': 'Expert',
                                           'options': [   'Access tables and rows in a consistent deterministic order '
                                                          'across transactions and keep transactions short',
                                                          'Set isolation level to READ UNCOMMITTED globally',
                                                          'Disable database foreign key checks permanently',
                                                          'Replace primary key B-Trees with Hash indexes on '
                                                          'auto-increment columns'],
                                           'q': 'When optimizing a transactional backend experiencing deadlock errors '
                                                'under high concurrent writes, what remediation is most effective?'}]},
    'UI/UX Designer': {   'Color Theory': [   {   'answer': 'Complementary',
                                                  'difficulty': 'Basic',
                                                  'options': ['Complementary', 'Analogous', 'Monochromatic', 'Triadic'],
                                                  'q': 'Which color scheme uses colors that sit directly opposite each '
                                                       'other on the color wheel?'},
                                              {   'answer': '60-30-10 Rule',
                                                  'difficulty': 'Beginner',
                                                  'options': [   '60-30-10 Rule',
                                                                 '80-20 Rule',
                                                                 'Golden Ratio',
                                                                 'Rule of Thirds'],
                                                  'q': 'What popular UI design rule recommends distributing colors in '
                                                       '60% dominant, 30% secondary, and 10% accent proportions?'},
                                              {   'answer': 'HSL allows intuitive mathematical adjustments of '
                                                            'lightness and saturation for hover/active states while '
                                                            'holding hue constant',
                                                  'difficulty': 'Intermediate',
                                                  'options': [   'HSL allows intuitive mathematical adjustments of '
                                                                 'lightness and saturation for hover/active states '
                                                                 'while holding hue constant',
                                                                 'HSL uses less memory in browser rendering engines',
                                                                 'HSL supports more total colors than HEX',
                                                                 'HSL automatically converts text into vector paths'],
                                                  'q': 'What is the functional advantage of using the HSL (Hue, '
                                                       'Saturation, Lightness) color model over HEX for UI design '
                                                       'system themes?'},
                                              {   'answer': 'By mapping functional roles (e.g. surface-primary, '
                                                            'text-on-surface) to dynamic tokens that rebind to '
                                                            'different primitive color values per theme mode',
                                                  'difficulty': 'Advanced',
                                                  'options': [   'By mapping functional roles (e.g. surface-primary, '
                                                                 'text-on-surface) to dynamic tokens that rebind to '
                                                                 'different primitive color values per theme mode',
                                                                 'By inverting raw HEX color values mathematically '
                                                                 'using negative CSS filters',
                                                                 'By forcing dark backgrounds across all app screens '
                                                                 'regardless of user settings',
                                                                 'By using pure black (#000000) and pure white '
                                                                 '(#FFFFFF) exclusively'],
                                                  'q': 'How do UI designers design accessible Light and Dark Theme '
                                                       'color systems using Semantic Tokens?'},
                                              {   'answer': 'Never rely solely on color to convey critical '
                                                            'information; supplement color states with iconography, '
                                                            'text labels, and structural patterns',
                                                  'difficulty': 'Expert',
                                                  'options': [   'Never rely solely on color to convey critical '
                                                                 'information; supplement color states with '
                                                                 'iconography, text labels, and structural patterns',
                                                                 'Increase screen brightness settings automatically',
                                                                 'Use only grayscale color palettes across the entire '
                                                                 'web application',
                                                                 'Replace colored buttons with standard underlined '
                                                                 'text links'],
                                                  'q': 'When designing digital interfaces for users with visual '
                                                       'impairments (e.g. Red-Green Color Blindness / Deuteranopia), '
                                                       'how do you ensure visual accessibility?'}],
                          'Figma': [   {   'answer': 'Auto Layout',
                                           'difficulty': 'Basic',
                                           'options': ['Auto Layout', 'Smart Animate', 'Components', 'Variants'],
                                           'q': 'Which Figma feature allows responsive layouts to adjust automatically '
                                                'when content changes?'},
                                       {   'answer': 'Variants',
                                           'difficulty': 'Beginner',
                                           'options': ['Variants', 'Auto Layout', 'Frames', 'Styles'],
                                           'q': 'What Figma feature groups related component variations (e.g. Hover, '
                                                'Active, Disabled states) into a single container?'},
                                       {   'answer': 'By storing reusable design decisions (colors, typography, '
                                                     'spacing) as structured JSON variables consumed directly by code '
                                                     'bases',
                                           'difficulty': 'Intermediate',
                                           'options': [   'By storing reusable design decisions (colors, typography, '
                                                          'spacing) as structured JSON variables consumed directly by '
                                                          'code bases',
                                                          'By exporting frames as flattened JPEG images',
                                                          'By generating HTML code automatically without CSS',
                                                          'By creating animated GIF files of screens'],
                                           'q': 'How do Figma Design Tokens streamline developer handoff across web '
                                                'and mobile platforms?'},
                                       {   'answer': 'Smart Animate',
                                           'difficulty': 'Advanced',
                                           'options': ['Smart Animate', 'Instant Transition', 'Dissolve', 'Push/Slide'],
                                           'q': 'What prototyping feature in Figma calculates transitions between '
                                                'matching layers across frames automatically?'},
                                       {   'answer': 'Separate foundational Primitive Tokens (colors, grid) from '
                                                     'Semantic Tokens (surface-primary) and Component Sets (buttons) '
                                                     'published as shared team libraries',
                                           'difficulty': 'Expert',
                                           'options': [   'Separate foundational Primitive Tokens (colors, grid) from '
                                                          'Semantic Tokens (surface-primary) and Component Sets '
                                                          '(buttons) published as shared team libraries',
                                                          'Place all screens and UI elements inside a single '
                                                          'unorganized canvas file',
                                                          'Detach component instances to edit properties directly on '
                                                          'screens',
                                                          'Export all UI components as SVG icons without variants'],
                                           'q': 'When architecting an enterprise Figma Design System for multi-brand '
                                                'applications, how should component library hierarchy be structured?'}],
                          'Prototyping': [   {   'answer': 'High-Fidelity Prototype',
                                                 'difficulty': 'Basic',
                                                 'options': [   'High-Fidelity Prototype',
                                                                'Low-Fidelity Prototype',
                                                                'Wireframe',
                                                                'Paper Prototype'],
                                                 'q': 'What level of fidelity is a prototype that includes realistic '
                                                      'visuals, interactive UI states, and realistic transitions?'},
                                             {   'answer': 'Micro-interactions',
                                                 'difficulty': 'Beginner',
                                                 'options': [   'Micro-interactions',
                                                                'Wireframes',
                                                                'Design Tokens',
                                                                'Style Guides'],
                                                 'q': 'What user feedback response triggers interactive visual changes '
                                                      'on hover or click in a prototype?'},
                                             {   'answer': 'They store dynamic user inputs and evaluate IF/ELSE '
                                                           'conditions to simulate real application data state changes',
                                                 'difficulty': 'Intermediate',
                                                 'options': [   'They store dynamic user inputs and evaluate IF/ELSE '
                                                                'conditions to simulate real application data state '
                                                                'changes',
                                                                'They write backend SQL database scripts automatically',
                                                                'They export iOS Swift code without layout constraints',
                                                                'They generate automated user testing recordings'],
                                                 'q': 'How do advanced prototyping tools (e.g. ProtoPie, Figma) '
                                                      'utilize Variables and Conditional Logic?'},
                                             {   'answer': 'Task Completion Rate (Direct Success)',
                                                 'difficulty': 'Advanced',
                                                 'options': [   'Task Completion Rate (Direct Success)',
                                                                'Net Promoter Score (NPS)',
                                                                'System Usability Scale (SUS)',
                                                                'Click-Through Rate (CTR)'],
                                                 'q': 'What usability testing metric measures the percentage of '
                                                      'participants who complete a prototype task successfully?'},
                                             {   'answer': 'Provide immediate tactile visual feedback, use progressive '
                                                           'disclosure to group input steps, and preserve user input '
                                                           'state dynamically across screens',
                                                 'difficulty': 'Expert',
                                                 'options': [   'Provide immediate tactile visual feedback, use '
                                                                'progressive disclosure to group input steps, and '
                                                                'preserve user input state dynamically across screens',
                                                                'Display all 25 form input fields on a single '
                                                                'unscrollable screen',
                                                                'Disable back button navigation between checkout steps',
                                                                'Hide validation error messages until final submit '
                                                                'button click'],
                                                 'q': 'When prototyping complex multi-step mobile checkout flows, how '
                                                      'do you design micro-interactions to minimize Cognitive Load?'}],
                          'Typography': [   {   'answer': 'Serif',
                                                'difficulty': 'Basic',
                                                'options': ['Serif', 'Sans-Serif', 'Monospace', 'Display'],
                                                'q': 'Which font classification is characterized by small decorative '
                                                     'strokes at the ends of character letterforms?'},
                                            {   'answer': 'Leading (Line Height)',
                                                'difficulty': 'Beginner',
                                                'options': [   'Leading (Line Height)',
                                                               'Kerning',
                                                               'Tracking',
                                                               'Baseline Offset'],
                                                'q': 'What term refers to the vertical distance between baselines of '
                                                     'lines of text?'},
                                            {   'answer': 'Kerning adjusts spacing between individual character pairs; '
                                                          'Tracking adjusts uniform spacing across an entire word or '
                                                          'passage',
                                                'difficulty': 'Intermediate',
                                                'options': [   'Kerning adjusts spacing between individual character '
                                                               'pairs; Tracking adjusts uniform spacing across an '
                                                               'entire word or passage',
                                                               'Tracking adjusts vertical line height; Kerning adjusts '
                                                               'horizontal font size',
                                                               'Kerning applies only to Serif fonts; Tracking applies '
                                                               'to Sans-Serif fonts',
                                                               'There is no difference'],
                                                'q': 'What is the key difference between Kerning and Tracking in '
                                                     'typography?'},
                                            {   'answer': '4.5:1',
                                                'difficulty': 'Advanced',
                                                'options': ['4.5:1', '3.0:1', '7.0:1', '2.0:1'],
                                                'q': 'What Web Content Accessibility Guidelines (WCAG 2.1 AA) contrast '
                                                     'ratio is required for normal body text against its background?'},
                                            {   'answer': 'Define min, viewport-preferred (`vw`), and max dynamic font '
                                                          'size bounds (`clamp(1rem, 2.5vw, 2.5rem)`) linked to '
                                                          'modular scale ratios',
                                                'difficulty': 'Expert',
                                                'options': [   'Define min, viewport-preferred (`vw`), and max dynamic '
                                                               'font size bounds (`clamp(1rem, 2.5vw, 2.5rem)`) linked '
                                                               'to modular scale ratios',
                                                               'Set static pixel (`px`) sizes inside fixed breakpoint '
                                                               'media queries for every screen pixel width',
                                                               'Multiply heading sizes by random floating point '
                                                               'numbers',
                                                               'Use monospace fonts exclusively across mobile '
                                                               'viewports'],
                                                'q': 'How do you construct a responsive Fluid Typographic Scale using '
                                                     'CSS `clamp()` for multi-device digital design systems?'}],
                          'Wireframing': [   {   'answer': 'To map out layout structure, page flow, and content '
                                                           'hierarchy without getting distracted by visual design '
                                                           'details',
                                                 'difficulty': 'Basic',
                                                 'options': [   'To map out layout structure, page flow, and content '
                                                                'hierarchy without getting distracted by visual design '
                                                                'details',
                                                                'To finalize exact visual brand color choices',
                                                                'To test micro-interaction animations',
                                                                'To export final production CSS stylesheets'],
                                                 'q': 'What is the primary purpose of a Low-Fidelity Wireframe?'},
                                             {   'answer': '12-Column Grid',
                                                 'difficulty': 'Beginner',
                                                 'options': [   '12-Column Grid',
                                                                '4-Column Fixed Grid',
                                                                'Isometric Grid',
                                                                'Golden Ratio Spiral Grid'],
                                                 'q': 'Which grid system is widely used in responsive wireframing for '
                                                      'web page layouts?'},
                                             {   'answer': 'User Flow / Task Flow',
                                                 'difficulty': 'Intermediate',
                                                 'options': [   'User Flow / Task Flow',
                                                                'Mood Board',
                                                                'Color Palette',
                                                                'Site Map'],
                                                 'q': 'What design artifact visually maps the sequence of steps a user '
                                                      'takes to complete a goal within an application?'},
                                             {   'answer': 'It organizes and structures digital content logically '
                                                           'based on user mental models, ensuring intuition in '
                                                           'navigation paths',
                                                 'difficulty': 'Advanced',
                                                 'options': [   'It organizes and structures digital content logically '
                                                                'based on user mental models, ensuring intuition in '
                                                                'navigation paths',
                                                                'It selects visual font pairing combinations',
                                                                'It calculates grid column pixel widths automatically',
                                                                'It handles database schema normalization'],
                                                 'q': 'How does Information Architecture (IA) shape wireframe layout '
                                                      'design?'},
                                             {   'answer': 'Validating whether user mental models match the navigation '
                                                           'structure and identifying points of confusion or drop-off '
                                                           'in key tasks',
                                                 'difficulty': 'Expert',
                                                 'options': [   'Validating whether user mental models match the '
                                                                'navigation structure and identifying points of '
                                                                'confusion or drop-off in key tasks',
                                                                'Evaluating visual color contrast ratios',
                                                                'Measuring visual render latency of graphics',
                                                                'Counting the number of UI buttons per screen'],
                                                 'q': 'When conducting early Usability Testing on low-fidelity '
                                                      'wireframe paper prototypes, what insight is most critical to '
                                                      'evaluate?'}]}}

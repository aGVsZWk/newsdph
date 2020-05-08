#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

#define ONE_SECOND 1000000
#define RANGE 10
#define PERIOD 2
#define NUM_THREADS 4 

// �������ݽṹ����ͣ������Ϣ
typedef struct {
	int *carpark; // ��һ���������� buffer ģ��ͣ����ͣ��λ
	int capacity; // ͣ�����ĳ�������
	int occupied; // ͣ�������г�����Ŀ
	int nextin;  // ��һ�������ĳ���ͣ��λ�ã��� carpark ���������±��ʾ��
	int nextout; // ��һ��ȡ�ߵĳ���ͣ��λ�ã��� carpark ���������±��ʾ��
	int cars_in; // ��¼ͣ�������복�����ܺ�
	int cars_out;  //��¼��ͣ��������ȥ�ĳ����ܺ�
	pthread_mutex_t lock; //�������������ýṹ�е����ݱ��̻߳���ķ�ʽʹ��
	pthread_cond_t space; //��������������ͣ�����Ƿ��п�λ��
	pthread_cond_t car;   //��������������ͣ�����Ƿ��г�
	pthread_barrier_t bar; //�߳�����
} cp_t;

static void * car_in_handler(void *cp_in);
static void * car_out_handler(void *cp_in);

static void * monitor(void *cp_in);
static void initialise(cp_t *cp, int size);


int main(int argc, char *argv[]) {

	if (argc != 2) {
		printf("Usage: %s carparksize\n", argv[0]);
		exit(1);
	}

	cp_t ourpark;

	initialise(&ourpark, atoi(argv[1])); // ��ʼ��ͣ�������ݽṹ

	pthread_t car_in, car_out, m;  // �����̱߳���
	pthread_t car_in2, car_out2;

	pthread_create(&car_in, NULL, car_in_handler, (void *)&ourpark);  // ������ͣ����ͣ���̣߳�������1��
	pthread_create(&car_out, NULL, car_out_handler, (void *)&ourpark); // ������ͣ����ȡ���̣߳�������1��
	pthread_create(&car_in2, NULL, car_in_handler, (void *)&ourpark); // ������ͣ����ͣ���̣߳�������2��
	pthread_create(&car_out2, NULL, car_out_handler, (void *)&ourpark); // ������ͣ����ȡ���̣߳�������2��
	pthread_create(&m, NULL, monitor, (void *)&ourpark);  // �������ڼ��ͣ����״�����߳�

	// pthread_join �ĵڶ�����������Ϊ NULL����ʾ���������̵߳ķ���״̬�������ȴ�ָ���̣߳���һ������������ֹ
	pthread_join(car_in, NULL);
	pthread_join(car_out, NULL);
	pthread_join(car_in2, NULL);
	pthread_join(car_out2, NULL);
	pthread_join(m, NULL);

	exit(0);
}

static void initialise(cp_t *cp, int size) {

	cp->occupied = cp->nextin = cp->nextout = cp->cars_in = cp->cars_out = 0;
	cp->capacity = size;  //����ͣ�����Ĵ�С

	cp->carpark = (int *)malloc(cp->capacity * sizeof(*cp->carpark));

	// ��ʼ���߳����ϣ�NUM_THREADS ��ʾ�ȴ� NUM_THREADS = 4 ���߳�ͬ��ִ�� 
	pthread_barrier_init(&cp->bar, NULL, NUM_THREADS);


	if (cp->carpark == NULL) {
		perror("malloc()");
		exit(1);
	}

	srand((unsigned int)getpid());

	pthread_mutex_init(&cp->lock, NULL); // ��ʼ��ͣ��������
	pthread_cond_init(&cp->space, NULL); // ��ʼ������ͣ�����Ƿ��п�λ����������
	pthread_cond_init(&cp->car, NULL); // ��ʼ������ͣ�����Ƿ��г�����������
}

static void* car_in_handler(void *carpark_in) {

	cp_t *temp;
	unsigned int seed;
	temp = (cp_t *)carpark_in;

	// pthread_barrier_wait �����������߳�����ɹ������ȴ������̸߳���
	pthread_barrier_wait(&temp->bar);
	while (1) {

		// ���߳��������һ��ʱ�䣬ģ�⳵�������ĵ������
		usleep(rand_r(&seed) % ONE_SECOND);

		pthread_mutex_lock(&temp->lock);

		// ѭ���ȴ�ֱ����ͣ��λ
		while (temp->occupied == temp->capacity)
			pthread_cond_wait(&temp->space, &temp->lock);

		// ����һ�����������������ʶ��
		temp->carpark[temp->nextin] = rand_r(&seed) % RANGE;

		// ��������������
		temp->occupied++;
		temp->nextin++;
		temp->nextin %= temp->capacity; // ѭ����������ͣ��λ��
		temp->cars_in++;

		// �����е����ڵ��г���ȡ���̣߳������Ƿ��� temp->car ��������
		pthread_cond_signal(&temp->car);

		// �ͷ���
		pthread_mutex_unlock(&temp->lock);

	}
	return ((void *)NULL);

}

static void* car_out_handler(void *carpark_out) {

	cp_t *temp;
	unsigned int seed;
	temp = (cp_t *)carpark_out;
	pthread_barrier_wait(&temp->bar);
	for (; ;) {

		// ���߳��������һ��ʱ�䣬ģ�⳵�������ĵ������
		usleep(rand_r(&seed) % ONE_SECOND);

		// ��ȡ����ͣ�����ṹ����
		pthread_mutex_lock(&temp->lock);

		/* ���������� temp->occupied ��������ʱ���������Ϊ0��occupied ==0 ����
		pthread_cond_wait ���еĲ�����æ�ȣ��ͷ�����&temp->lock���������߳�ʹ�á�
		ֱ�� &temp->car �����ı�ʱ�ٴν�����ס */
		while (temp->occupied == 0)
			pthread_cond_wait(&temp->car, &temp->lock);

		// ������Ӧ������
		temp->occupied--; // ���г�����Ŀ��1
		temp->nextout++;
		temp->nextout %= temp->capacity;
		temp->cars_out++;


		// �����е����ڵ��пտճ�λ���̣߳������Ƿ��� temp->space ��������
		pthread_cond_signal(&temp->space);

		// �ͷű���ͣ�����ṹ����
		pthread_mutex_unlock(&temp->lock);

	}
	return ((void *)NULL);

}

// ���ͣ����״��
static void *monitor(void *carpark_in) {

	cp_t *temp;
	temp = (cp_t *)carpark_in;

	for (; ;) {
		sleep(PERIOD);

		// ��ȡ��
		pthread_mutex_lock(&temp->lock);
		
		/* ֤�������Ʊ�֤�߳�ʵ�ֵ�������������ģ����ȷ�ķ�ʽ�ǣ�
		temp->cars_in - temp->cars_out - temp->occupied == 0�����ܵĽ����ĳ� == 
		�ܵĿ���ȥ�ĳ� +��ͣ�������еĳ� */
		printf("Delta: %d\n", temp->cars_in - temp->cars_out - temp->occupied);
		printf("Number of cars in carpark: %d\n", temp->occupied);

		// �ͷ���
		pthread_mutex_unlock(&temp->lock);

	}

	return ((void *)NULL);
}
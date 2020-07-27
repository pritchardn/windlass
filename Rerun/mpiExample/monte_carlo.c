#include<stdio.h>
#include<mpi.h>
#include<stdlib.h>
#include <time.h>

int main(int argc, char *argv[]){
	int rank, size, i;
	double x=0,y=0,pi,z;
	int no = atoi(argv[1]);
	int count=0,total_count=0,no_div=0,fin_no = 0;
	MPI_Init(&argc, &argv);
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	printf("Hello from Rank %d\n", rank);
	no_div = no/size;
	srand(42);
	for(i = 0; i < no_div; ++i){
		x = (rand()%100) / (double)100;
		y = (rand()%100) / (double)100;
		z = x*x + y*y;
		if(z <=1)
			count++;
	}
	MPI_Reduce(&count,&total_count,1,MPI_INT,MPI_SUM,0,MPI_COMM_WORLD);
	MPI_Reduce(&no_div,&fin_no,1,MPI_INT,MPI_SUM,0,MPI_COMM_WORLD);

	if(rank == 0){
		printf("Total count  = %d, total itrr = %d\n",total_count,fin_no);
		pi = ((double)total_count)/fin_no*4.0000;
		FILE *fp;
		fp = fopen("./mpi_result.out", "w");
		fprintf(fp, "%lf\n", pi);
		fclose(fp);
	}
	MPI_Finalize();
}
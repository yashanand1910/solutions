/**
 * @input A : Read only ( DON'T MODIFY ) Integer array
 * @input n1 : Integer array's ( A ) length
 * 
 * @Output string. Make sure the string ends with null character
 */
int comp (const void * elem1, const void * elem2) 
{
    long f = (long)*((int*)elem1);
    long s = (long)*((int*)elem2);
    int counts = 1;
    int countf = 1;
    int temp;
    temp = s;
    int i;
    while(1)
    {
        temp = temp/10;
        counts = counts *10;
    
        if(temp ==0)
        {
            break;
        }
    }
    temp = f;
     while(1)
    {
        temp = temp/10;
        countf = countf*10;
    
        if(temp ==0)
        {
            break;
        }
    }
        
    //printf("The two number f*pow(10,counts) + s = %d s*pow(10,countf) + f = %d \n", f*counts + s, s*countf + f);
    
    if (f*counts + s > s*countf + f) return 1;
    if (f*counts + s < s*countf + f) return -1;
    return 0;
}
 
 
char* largestNumber(const int* A, int n1) {

    int i = 0;

    if(n1 > 1)
    {
        qsort (A, n1, sizeof(int), comp);    
    }
    
    int flag = 0;
    for(i = 0; i < n1; i++)
    {
        if(A[i] > 0)
        {
            flag = 1;
        }
    }

    if(flag ==0)
    {
        char *s = (char *)malloc(2*sizeof(char));
        s[0] = '0';
        s[1] = '\0';
        return s;
    }





    // for(i = 0; i < n1; i++)
    // {
    //     printf("%d\n", A[i]);
    // }
    int counts[n1];
    int count = 0;
    int temp;
    for(i = 0; i < n1; i++)
    {
        temp = A[i];
        counts[i] = 0;
        while(1)
        {
            temp = temp/10;
            counts[i] = counts[i] + 1;
            count = count + 1;
            if(temp ==0)
            {
                break;
            }
        }
    }
    
    char *result = (char *)malloc((count + 1)*(sizeof(char)));
    int k = 0;
    
    for(i = n1-1; i >= 0; i--)
    {
        temp = A[i];
        int temp2 = counts[i];
        // printf("A[i] = %d, count = %d total count = %d \n", A[i], counts[i], count);
        while(1)
        {
            result[k + counts[i] - 1] = '0' + temp%10; 
            
            temp = temp/10;
            counts[i] = counts[i] -1;
            if(temp==0)
            {
                break;
            }
        }
        k = k + temp2;
            
        
    }
    
    // for(i = 0; i < count; i++)
    // {
    //     printf("%c\n", result[i]);
    // }
    
    
    // char *num[n1];
    // int total_count = 0;
    // for ( i = 0; i < n1; i++)
    // {
    //     int temp = A[i];
    //     int count = 0;
    //     while(temp > 0)
    //     {
    //         temp = temp/10;
    //         count = count + 1;
    //         total_count++;
    //     }
        
    //     num[i] = ( char*)malloc(count*sizeof(char));
    //     int j = 0;
    //     temp = A[i];
    //     for(j = count - 1; j >=0;j--)
    //     {
    //         num[i][j] = temp%10;
    //         temp = temp/10;
    //     }
        
    // }
    // int rank[n1];
    // for(i = 0; i < n1; i++)
    // {
    //     rank[i] = 0;
    // }
    
    // for(i = 0; i < n1; i++)
    // {
    //     for(j = 0; j < n1-1; j++)
    //     {
    //         if(num[j][0] > num[rank[i]][0])
    //         {
    //             rank[i] = j;
    //         }
            
    //         else if(num)
    //     }
    // }
    result[count] =  '\0';
    return result;
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   corsair.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/04/27 17:09:04 by preina-g          #+#    #+#             */
/*   Updated: 2023/05/05 14:02:37 by preina-g         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <openssl/rsa.h>
#include <openssl/engine.h>
#include <openssl/err.h>
#include <openssl/bio.h>
#include <openssl/bn.h>
#include <openssl/evp.h>
#include <openssl/x509.h>
#include <openssl/pem.h>

#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <math.h>


typedef struct data
{
    RSA *rsa_pub1;
    RSA *rsa_pub2;
    RSA *rsa_priv;
    BIGNUM *n1;
    BIGNUM *n2;
    BIGNUM *q1;
    BIGNUM *q2;
    BIGNUM *e;
    BIGNUM *p;
    BIGNUM *d;
    BIGNUM *one;
    BIGNUM *totient;
    BIGNUM *fi1;
    BIGNUM *fi2;
    BN_CTX *ctx;
    BIO *certbio;
    BIO *certbio2;
    
}rsa_data;

RSA *init_rsa(char *path, rsa_data *data)
{
    data->certbio = BIO_new_file(path, "r");
	RSA *pubkey = NULL;
    if (!data->certbio)
        exit(printf("Can't read cerrtificates."));
	BIO_read_filename(data->certbio, path);
    PEM_read_bio_RSA_PUBKEY(data->certbio, &pubkey, NULL, NULL);
    return pubkey;
}

RSA *init_rsa2(char *path, rsa_data *data)
{
    data->certbio2 = BIO_new_file(path, "r");
	RSA *pubkey = NULL;
    if (!data->certbio2)
        exit(printf("Can't read cerrtificates."));
	BIO_read_filename(data->certbio, path);
    PEM_read_bio_RSA_PUBKEY(data->certbio, &pubkey, NULL, NULL);
    return pubkey;
}


void set_priv_key(rsa_data *data)
{
    data->rsa_priv = RSA_new();
    RSA_set0_key(data->rsa_priv, BN_dup(data->n1), BN_dup(data->e), BN_dup(data->d));
    RSA_set0_factors(data->rsa_pub1, data->p, data->q1);
    RSA_set0_factors(data->rsa_pub2, data->p, data->q2);
}

void decrypt_msg(rsa_data *data, char *path)
{
    unsigned char *encrypt;
    unsigned char *msg;
    int fd = open(path, O_RDONLY);
    if (!fd)
        exit(printf("There are not encrypted msg"));
    encrypt = (unsigned char *)malloc(sizeof(unsigned char) * 1024);
    msg = (unsigned char *)malloc(sizeof(unsigned char) * 1024);
    int len = read(fd, encrypt, 1024);
    RSA_private_decrypt(len, encrypt, msg, data->rsa_priv, RSA_PKCS1_PADDING);
    if (msg != NULL)
    {
        printf("\n MESSAGE \n");
        printf("%s\n", msg);
    }
    else
        printf("THERE ARE NOT MESSAGE");
    close(fd);
    free(msg);
    free(encrypt);
}


void get_pair_of_primes(rsa_data *data, char *msg)
{
    //iniocializa los bignum
    data->p = BN_new();
    data->ctx = BN_CTX_new();
    data->q1 = BN_new();
    data->q2 = BN_new();
    data->d = BN_new();
    data->totient = BN_new();
    data->fi1 = BN_new();
    data->fi2 = BN_new();
    //recoge los modilos y el exponete
    data->n1 = (BIGNUM *)RSA_get0_n(data->rsa_pub1);//get the value modulus n1
    data->n2 = (BIGNUM *)RSA_get0_n(data->rsa_pub2);//get the value modulus n2
    data->e = (BIGNUM *)RSA_get0_e(data->rsa_pub1);//get the exponent e
    BN_gcd(data->p, data->n1, data->n2, data->ctx); // get the gcd that is the first prime
    if (!BN_is_one(data->p) && BN_cmp(data->n1, data->n2) != 0) // if p is not 1 get the other prime
    {
        BN_div(data->q1, NULL, data->n1, data->p, data->ctx); //get the other prime q1 from n1
        BN_div(data->q2, NULL, data->n2, data->p, data->ctx); //get the other prime q2 from n2
        //calculate the totient from euclidean algorithm
        BN_sub(data->fi1, data->q1, BN_value_one());
        BN_sub(data->fi2, data->p, BN_value_one());
        BN_mul(data->totient, data->fi1, data->fi2, data->ctx);
        BN_mod_inverse(data->d, data->e, data->totient, data->ctx); //calculates d from totient and exponent
        set_priv_key(data);
        decrypt_msg(data, msg);
    }
    else
        printf("THEY ARE NOT VULNERABLE\n");
}

void ft_l()
{
    system("leaks corsair");
}
void ft_free(rsa_data *data)
{
    BN_CTX_free(data->ctx);                      
    BN_free(data->d);
    BN_free(data->totient);                    
    BN_free(data->fi1);                      
    BN_free(data->fi2);
    BIO_free_all(data->certbio);
    BIO_free_all(data->certbio2);
    RSA_free(data->rsa_pub1);
    RSA_free(data->rsa_pub2);
    RSA_free(data->rsa_priv);
}

int main(int argc, char **argv)
{
    if (argc == 4)
    {
        rsa_data data;
        data.rsa_pub1 = init_rsa(argv[1], &data);
        data.rsa_pub2 = init_rsa2(argv[2], &data);
        printf("%s -- %s -- %s\n", argv[1], argv[2], argv[3]);
        get_pair_of_primes(&data, argv[3]);
        ft_free(&data);
    }
    else
        printf("USAGE:\n\t./corsair <cert1.pem> <cert2.pem> <encripted msg>");
    return 0;
}

/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   vuln.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: preina-g <preina-g@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/05/08 16:23:41 by preina-g          #+#    #+#             */
/*   Updated: 2023/05/13 13:56:34 by preina-g         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <string.h>
#include <stdio.h>  // librería stdio.h, funciones básicas de Entrada/Salida

int main (int argc, char **argv){  // La función "principal" del programa
    char buffer[64]; //Declaramos un array con 64 bytes de espacio
    if (argc < 2){  // Si los argumentos son menores que 2...
        printf ("Introduzca un argumento al programa\n"); //Printeamos   
        return 0;  // y retornamos 0 a la función main, y el programa acaba
    }
    else
        strcpy(buffer, argv[1]); // Aqui es donde esta el fallo.

    return 0;  // Devolvemos 0 a main, y el programa acaba
}
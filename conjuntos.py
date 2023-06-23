{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "8e92344d",
   "metadata": {},
   "source": [
    "# Conjuntos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cb15d596",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 3, 4, 76, 45, 14.56, 243, -1, -4, -2}\n"
     ]
    }
   ],
   "source": [
    "# Criando um conjunto (números repetidos aparecem apenas uma vez)\n",
    "\n",
    "teste_conjunto = set([1, 4, 45, 76, -2, 243, 14.56, -2, 4, 3, 4, -4, -1, 1])\n",
    "print(teste_conjunto)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3789f058",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 34, 5.34, -5.34, -4, -2}\n"
     ]
    }
   ],
   "source": [
    "teste_conjunto2 = {34, 34, -4, 5.34, 1, -2, 1, -5.34, 5.34}\n",
    "print(teste_conjunto2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "2d2efe7f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{1, 2, 3, 4, 5, 7, 9, 42, 11, -5.67, 31}\n",
      "[1, 2, 3, 4, 5, 7, 9, 11, 31, 11, 2, 42, -5.67, 4]\n"
     ]
    }
   ],
   "source": [
    "lista = [1, 2, 3, 4, 5, 7, 9, 11, 31, 11, 2, 42, -5.67, 4] #??????????????\n",
    "conjunto_3=set(lista)\n",
    "print(conjunto_3) #printa como conjunto\n",
    "print(lista) #printa o objeto lista que é uma lista"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "75008037",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 3, 5, 23, -2}\n"
     ]
    }
   ],
   "source": [
    "conjunto_3 = {1, 3, 3, 5, 5, 0, 0, 23, -2}\n",
    "print(conjunto_3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "8fd95530",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 2, 3, 5, 23, 42, -2}\n"
     ]
    }
   ],
   "source": [
    "conjunto_3.add(42) # Adiciona 42 ao conjunto\n",
    "print(conjunto_3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "751f64e4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{0, 1, 2, 3, 5, 23, -2}\n"
     ]
    }
   ],
   "source": [
    "conjunto_3.remove(42)\n",
    "print(conjunto_3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cfc664b4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

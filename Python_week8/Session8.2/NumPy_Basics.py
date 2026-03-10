{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "59b9bf5c-d02b-48db-9226-3ac5eb8c5440",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "337f3e30-43a6-4b74-a24e-99efe3e612bb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5]\n"
     ]
    }
   ],
   "source": [
    "#Create array from list\n",
    "arr = np.array([1, 2, 3, 4, 5])\n",
    "print(arr)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7892dbd3-042b-41bf-a7d4-8580cb1b2c32",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 2  4  6  8 10]\n"
     ]
    }
   ],
   "source": [
    "#Mathematical operations(vectorized!)\n",
    "print(arr * 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7b07c690-c03f-418e-a200-39ee70797933",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[11 12 13 14 15]\n"
     ]
    }
   ],
   "source": [
    "print(arr + 10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "d7a49087-a442-4421-86b7-438473ada019",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 1  4  9 16 25]\n"
     ]
    }
   ],
   "source": [
    "print(arr ** 2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "351bd6f4-f83a-42fa-ae3b-f4b1900bd2d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "# works on ALL elements at once!\n",
    "# much faster than loops\n",
    "# 2D array (matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "21b9f9d6-1956-487e-8d3e-af77c6e639d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "matrix = np.array([[1, 2, 3], [4, 5, 6]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ea215703-2748-4a21-9a2a-7bfe55b2c7ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1 2 3]\n",
      " [4 5 6]]\n"
     ]
    }
   ],
   "source": [
    "print(matrix)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0120612e-4496-457b-acc4-ce1c07c3617e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

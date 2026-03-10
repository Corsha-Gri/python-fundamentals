{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e9574c43-f2dc-4cda-a59d-18f6601282ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "eb6e3ef1-9079-4cac-ab8a-1371c5b92693",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create DataFrame from dict\n",
    "data = {\n",
    "    'name': ['Alice', 'Bob', 'Carol'],\n",
    "    'age': [25, 30, 28],\n",
    "    'score': [95, 87, 92]\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1ec92112-1391-4167-9da7-0b00db179061",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    name  age  score\n",
      "0  Alice   25     95\n",
      "1    Bob   30     87\n",
      "2  Carol   28     92\n"
     ]
    }
   ],
   "source": [
    "df = pd.DataFrame(data)\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "94488842-02f1-45b0-9aee-1a7ebe679d1e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    Alice\n",
      "1      Bob\n",
      "2    Carol\n",
      "Name: name, dtype: object\n"
     ]
    }
   ],
   "source": [
    "#Access columns\n",
    "print(df['name'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "faeb5170-1ac5-4c5a-8069-3f9c176ed580",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    name  age  score\n",
      "0  Alice   25     95\n",
      "2  Carol   28     92\n"
     ]
    }
   ],
   "source": [
    "#Filter rows\n",
    "high_scores = df[df['score'] >= 90]\n",
    "print(high_scores)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d361303-5233-4039-9464-636a364bd9fd",
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

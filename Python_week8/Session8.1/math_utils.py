{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "d2e5b3ad-ebb0-4ad4-9dc1-0dcb01bb25b2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting math_utils.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile math_utils.py\n",
    "def add(a, b):\n",
    "    return a + b\n",
    "def multiply(a, b):\n",
    "    return a * b\n",
    "def calculate_average(numbers):\n",
    "    return sum(numbers) / len(numbers)\n",
    "PI = 3.14159"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "4d05c93e-98a3-4841-8210-4d5e271c16a4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15\n",
      "20.0\n",
      "20\n",
      "3.14159\n"
     ]
    }
   ],
   "source": [
    "# File: main.py (in same directory as math_utils.py)\n",
    "# Method 1: Import module\n",
    "import math_utils\n",
    "result = math_utils.add(10, 5)\n",
    "print(result)  # 15\n",
    "avg = math_utils.calculate_average([10, 20, 30])\n",
    "print(avg)  # 20.0\n",
    "# Method 2: Import specific functions\n",
    "from math_utils import multiply, PI\n",
    "result = multiply(4, 5)\n",
    "print(result)  # 20\n",
    "print(PI)  # 3.14159\n",
    "# Reusing code across files!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "dc251d14-1324-4941-bf39-ec179587213a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing data_tools/__init__.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile data_tools/__init__.py\n",
    "\n",
    "# directory structure:\n",
    "# data_tools /\n",
    "#     __init__.py\n",
    "#     readers.py\n",
    "#     writers.py\n",
    "#     validators.py\n",
    "# File: data_tools/ __init__.py\n",
    "# (can be empty or contain imports)\n",
    "\n",
    "# File: data_tools/readers.py\n",
    "def read_csv(filename):\n",
    "    # code\n",
    "    pass\n",
    "# File: data_tools/writers.py\n",
    "def write_csv(filename, data):\n",
    "    # code\n",
    "    pass\n",
    "# Now you have a package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "b6d6c10f-f3ca-4e78-bfa3-a61415f8e8d7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Reading CSV from file.csv\n",
      "Writing data to out.csv: ['header', 'data1', 'data2']\n",
      "Reading CSV from file.csv\n",
      "Writing data to out.csv: ['header', 'data1', 'data2']\n"
     ]
    }
   ],
   "source": [
    "# Import from package\n",
    "from data_tools import readers\n",
    "from data_tools import writers\n",
    "\n",
    "#Use Modules\n",
    "data = readers.read_csv('file.csv')\n",
    "writers.write_csv('out.csv', data)\n",
    "\n",
    "#Or import specific functions\n",
    "from data_tools.readers import read_csv\n",
    "from data_tools.writers import write_csv\n",
    "data = read_csv('file.csv')\n",
    "write_csv('out.csv', data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "fc24cb5d-785d-4c4b-866c-f402c3258b94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mkdir: data_tools: File exists\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "UsageError: Line magic function `%%writefile` not found.\n"
     ]
    }
   ],
   "source": [
    "!mkdir data_tools\n",
    "%%writefile data_tools/__init__.py\n",
    "# This file makes data_tools a Python package"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "7c2cd9d6-a267-4272-b077-1562aef01b09",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing data_tools/readers.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile data_tools/readers.py\n",
    "def read_csv(filename):\n",
    "    print(f\"Reading CSV from {filename}\")\n",
    "    # In a real scenario, this would read data from the file\n",
    "    return [\"header\", \"data1\", \"data2\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "ee21b46a-d36e-4749-9a91-ffabad11e2bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing data_tools/writers.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile data_tools/writers.py\n",
    "def write_csv(filename, data):\n",
    "    print(f\"Writing data to {filename}: {data}\")\n",
    "    # In a real scenario, this would write data to the file\n",
    "    pass"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "dde9ecf1-085f-4cbd-84a9-890f1afe7ea8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Testing math_utils...\n",
      "5 + 3 = 8\n",
      "4 * 5 = 20\n",
      "Test passed!\n"
     ]
    }
   ],
   "source": [
    "# File: math_utils.py\n",
    "def add(a, b):\n",
    "    return a+ b\n",
    "def multiply(a, b):\n",
    "    return a * b\n",
    "\n",
    "# Test code(only runs when executed directly)\n",
    "if __name__ == '__main__':\n",
    "    print('Testing math_utils...')\n",
    "    print(f'5 + 3 = {add(5, 3)}')\n",
    "    print(f'4 * 5 = {multiply(4, 5)}')\n",
    "    print('Test passed!')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "2ffc0b21-70e5-4ed4-ae4c-bc1faef6039a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#run directly: pyhton math_utils.py -> runs tests\n",
    "#import: from math_utils import add -> tests don't run\n",
    "# Perfect for module testing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47185e94-9b9d-4ba9-99b4-eb55c18634a2",
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

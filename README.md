# Yet Another Bencoder
As if we need more.

## Usage

You can install the latest commit of the package directly from the GitHub repository using the following command:
```bash
python3 -m pip install git+https://github.com/ethanavatar/yet-another-bencoder.git
```

The package contains two modules that can be used independently, each containing only their respective member functions.
```python
import bencoder
bencoder.encode('foo') # returns '3:foo'

import bdecoder
bdecoder.decode('3:bar') # returns 'bar'
```
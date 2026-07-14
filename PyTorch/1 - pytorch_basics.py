import torch
import numpy as np

# 1. TENSOR CREATION
x = torch.empty(2,3,2)
y = torch.rand(2,2)
y1 = torch.ones(2,2)
y2 = torch.zeros(2,2, dtype=torch.int64)
x1 = torch.tensor([2.5, 0.1])

print("y tensor:\n", y)
print("y dtype:", y.dtype)
print("y size:", y.size())

# 2. MATH OPERATIONS
z = y + y1
z = torch.add(y, y1) 

# FIXED: In-place addition (the _ symbol). 
# The tensor being added must match the shape of the target tensor.
y.add_(y1) 
print("y after in-place addition:\n", y) 

z1 = y - y1
z1 = torch.sub(y, y1)
z2 = y * y1
z2 = torch.mul(y, y1)

# 3. SLICING & RESHAPING
print("Slicing column 0 of y:\n", y[:,0]) 
print("1 element of y as standard python number:", y[1,1].item()) 

# Reshaping x from (2,3,2) to a 2D tensor of (something, 8). 
# Note: 2*3*2 = 12 total elements. You can't reshape 12 elements into groups of 8!
# FIXED: Let's reshape it into groups of 4 instead. 12 / 4 = 3 rows.
x_reshaped = x.view(-1, 4) 
print("Reshaped x size:", x_reshaped.size())

# 4. NUMPY BRIDGE
y_np = y1.numpy() 

a = np.ones(5)
# FIXED: from_numpy doesn't accept a 'dtype' argument directly. Cast it after.
a_torch = torch.from_numpy(a).to(torch.int64)
print("Torch tensor from Numpy:", a_torch)

# 5. CUDA / GPU MOVEMENT
if torch.cuda.is_available():
    print("CUDA is available! Moving tensors to GPU...")
    device = torch.device("cuda")
    x_gpu = torch.ones(5, device=device) 
    y_gpu = torch.ones(5) 
    y_gpu = y_gpu.to(device) 
    z_gpu = x_gpu + y_gpu 
    
    # z_gpu.numpy() # This will give an error as numpy expects CPU
    z_cpu = z_gpu.to("cpu") 
    print("Successfully brought tensor back to CPU for Numpy:", z_cpu.numpy())
else:
    print("CUDA not available on this environment.")

# 6. GRADIENT TRACKING
f = torch.ones(5, requires_grad=True)

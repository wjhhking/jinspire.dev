import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def draw_matrix(ax, width, height, pos_x, pos_y, label=None, color='skyblue', alpha=0.7):
    """Draw a rectangle representing a matrix with the given dimensions."""
    rect = patches.Rectangle((pos_x, pos_y), width, height, linewidth=1, 
                            edgecolor='black', facecolor=color, alpha=alpha)
    ax.add_patch(rect)
    
    # Add label in the middle of the rectangle if it fits
    if label:
        if width > len(label) * 5 and height > 10:  # Simple check if label might fit
            ax.text(pos_x + width/2, pos_y + height/2, label,
                    horizontalalignment='center', verticalalignment='center')
        else:
            # Place label outside if rectangle is too small
            ax.text(pos_x + width/2, pos_y + height + 5, label,
                    horizontalalignment='center', verticalalignment='bottom', fontsize=8)

# Set up the plot
fig, ax = plt.subplots(figsize=(20, 12))

# Dimensions
A_rows, A_cols = 5000, 768
B1_rows, B1_cols = 768, 768
B2_rows, B2_cols = 768, 3072
B3_rows, B3_cols = 3072, 768

# Use consistent scaling to maintain proper ratios
unit_scale = 0.02  # Each unit in matrices gets this many plot units

# Positions
margin = 20
start_x = margin
start_y = margin

# Draw matrix A
A_width = A_cols * unit_scale
A_height = A_rows * unit_scale
draw_matrix(ax, A_width, A_height, start_x, start_y, 
            label=f"A: {A_rows}×{A_cols}", color='lightblue')

# Position for B matrices start after A with some margin
B_start_x = start_x + A_width + margin * 2

# Draw 12 copies of matrix B (6 rows, 2 columns arrangement)
for i in range(6):
    for j in range(2):
        idx = i*2 + j
        
        # Calculate positions
        x_offset = j * (B1_cols * unit_scale + B2_cols * unit_scale + B3_cols * unit_scale + margin * 2)
        
        # Each row position depends on the height of B matrices in previous rows
        if i == 0:
            y_pos = start_y
        else:
            # Use the maximum height of B1, B2, B3 to position the next row
            max_B_height = max(B1_rows, B3_rows) * unit_scale
            y_pos = start_y + i * (max_B_height + margin)
        
        # Draw B1
        B1_width = B1_cols * unit_scale
        B1_height = B1_rows * unit_scale
        draw_matrix(ax, B1_width, B1_height, 
                    B_start_x + x_offset, 
                    y_pos,
                    label=f"B1 #{idx+1}: {B1_rows}×{B1_cols}", 
                    color='lightgreen')
        
        # Draw B2
        B2_width = B2_cols * unit_scale
        B2_height = B2_rows * unit_scale
        draw_matrix(ax, B2_width, B2_height, 
                    B_start_x + x_offset + B1_width + margin, 
                    y_pos,
                    label=f"B2 #{idx+1}: {B2_rows}×{B2_cols}", 
                    color='lightsalmon')
        
        # Draw B3
        B3_width = B3_cols * unit_scale
        B3_height = B3_rows * unit_scale
        draw_matrix(ax, B3_width, B3_height, 
                    B_start_x + x_offset + B1_width + B2_width + margin * 2, 
                    y_pos,
                    label=f"B3 #{idx+1}: {B3_rows}×{B3_cols}", 
                    color='lightpink')

# Add title and labels
ax.set_title("Matrix Visualization with Correct Aspect Ratios")
ax.set_xlabel("Columns (width)")
ax.set_ylabel("Rows (height)")

# Set aspect ratio to equal
ax.set_aspect('equal')

# Calculate the total width and height needed
total_width = B_start_x + 2 * (B1_cols * unit_scale + B2_cols * unit_scale + B3_cols * unit_scale + margin * 3) + margin
total_height = start_y + 6 * (max(B1_rows, B3_rows) * unit_scale + margin) + margin

# Set limits with some extra padding
ax.set_xlim(0, total_width * 1.05)
ax.set_ylim(0, total_height * 1.05)

# Show the plot
plt.tight_layout()
plt.show()

# Print actual dimensions for reference
print(f"Matrix A: {A_rows} × {A_cols}")
print(f"Matrix B1: {B1_rows} × {B1_cols}")
print(f"Matrix B2: {B2_rows} × {B2_cols}")
print(f"Matrix B3: {B3_rows} × {B3_cols}")
print(f"Total B matrix sets: 12 (6 rows × 2 columns)")
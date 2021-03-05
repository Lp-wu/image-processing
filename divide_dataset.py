import os
import glob

ex_c_orginal_np = 'expanded_sorce_4D'
po_c_orginal_np = 'point_sorce_4D'
ex_d_orginal_np = 'expanded_dirty'
po_d_orginal_np = 'point_dirty'

train_clean_set = 'data/Train/clean'
train_dirty_set = 'data/Train/dirty'
val_clean_set = 'data/Train/val_clean'
val_dirty_set = 'data/Train/val_dirty'
test_clean_set = 'data/Test/t_clean'
test_dirty_set = 'data/Test/t_dirty'

#划分expanded数据
ex_c_files =  glob.glob(os.path.join(ex_c_orginal_np,'*.npy'))
ex_c_files.sort()
ex_d_files =  glob.glob(os.path.join(ex_d_orginal_np,'*.npy'))
ex_d_files.sort()
for ex_num in range(len(ex_c_files)):
  ex_c_filename = os.path.basename(ex_c_files[ex_num])
  ex_d_filename = os.path.basename(ex_d_files[ex_num])
  ex_name, ex_ext = os.path.splitext(ex_c_filename)
  ex_c_src = os.path.join(os.path.abspath(ex_c_orginal_np),ex_c_filename)
  ex_d_src = os.path.join(os.path.abspath(ex_d_orginal_np),ex_d_filename)
  if (ex_num+1) <= 2800:
    train_c_dst = os.path.join(os.path.abspath('ex_'+train_clean_set),'train_c_'+str(ex_num+1)+ex_ext)
    os.rename(ex_c_src,train_c_dst)
    train_d_dst = os.path.join(os.path.abspath('ex_'+train_dirty_set),'train_d_'+str(ex_num+1)+ex_ext)
    os.rename(ex_d_src,train_d_dst)
  elif  (ex_num+1)>2800 and (ex_num+1) <= 3600:
    val_c_dst = os.path.join(os.path.abspath('ex_'+val_clean_set),'val_c_'+str(ex_num+1)+ex_ext)
    os.rename(ex_c_src,val_c_dst)
    val_d_dst = os.path.join(os.path.abspath('ex_'+val_dirty_set),'val_d_'+str(ex_num+1)+ex_ext)
    os.rename(ex_d_src,val_d_dst)
  else:
    test_c_dst = os.path.join(os.path.abspath('ex_'+test_clean_set), 'test_c_'+str(ex_num+1)+ex_ext)
    os.rename(ex_c_src,test_c_dst)
    test_d_dst = os.path.join(os.path.abspath('ex_'+test_dirty_set), 'test_d_'+str(ex_num+1)+ex_ext)
    os.rename(ex_d_src,test_d_dst)

#划分point数据
po_c_files =  glob.glob(os.path.join(po_c_orginal_np,'*.npy'))
po_c_files.sort()
po_d_files =  glob.glob(os.path.join(po_d_orginal_np,'*.npy'))
po_d_files.sort()
for po_num in range(len(po_c_files)):
  po_c_filename = os.path.basename(po_c_files[po_num])
  po_d_filename = os.path.basename(po_d_files[po_num])
  po_name, po_ext = os.path.splitext(po_c_filename)
  po_c_src = os.path.join(os.path.abspath(po_c_orginal_np),po_c_filename)
  po_d_src = os.path.join(os.path.abspath(po_d_orginal_np),po_d_filename)
  if (po_num+1) <= 2800:
    train_c_dst = os.path.join(os.path.abspath('po_'+train_clean_set),'train_c_'+str(po_num+1)+po_ext)
    os.rename(po_c_src,train_c_dst)
    train_d_dst = os.path.join(os.path.abspath('po_'+train_dirty_set),'train_d_'+str(po_num+1)+po_ext)
    os.rename(po_d_src,train_d_dst)
  elif  (po_num+1)>2800 and (po_num+1) <= 3600:
    val_c_dst = os.path.join(os.path.abspath('po_'+val_clean_set),'val_c_'+str(po_num+1)+po_ext)
    os.rename(po_c_src,val_c_dst)
    val_d_dst = os.path.join(os.path.abspath('po_'+val_dirty_set),'val_d_'+str(po_num+1)+po_ext)
    os.rename(po_d_src,val_d_dst)
  else:
    test_c_dst = os.path.join(os.path.abspath('po_'+test_clean_set), 'test_c_'+str(po_num+1)+po_ext)
    os.rename(po_c_src,test_c_dst)
    test_d_dst = os.path.join(os.path.abspath('po_'+test_dirty_set), 'test_d_'+str(po_num+1)+po_ext)
    os.rename(po_d_src,test_d_dst)


















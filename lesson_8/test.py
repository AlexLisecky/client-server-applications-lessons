my_dict = {
    1:'sdd',
    2:'hdd'
}
msg = []
for i in my_dict.keys():
    msg.append(i)

print(msg)
msg = [str(i) for i in msg]
new_str = ' '.join(msg)
print(new_str)
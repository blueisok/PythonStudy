print("邀请名单")
invites=["刘","李","忘"]
print(invites)
for invite in invites:
    print(f"{invite}先生很高兴邀请你")
print(f"{invite}先生没有时间,无法参加,请王先生代参加")
invites[2]="王"
print(invites)
for invite1 in invites:
    print(f"{invite1}先生很高兴邀请你")
print("我们有更大的餐桌")
print("有陈先生,白先生,杜先生加入我们")
invites.append("陈")
invites.insert(2,"白")
invites.insert(0,"杜")
print(invites)
for invite2 in invites:
    print(f"{invite2}先生很高兴邀请你")

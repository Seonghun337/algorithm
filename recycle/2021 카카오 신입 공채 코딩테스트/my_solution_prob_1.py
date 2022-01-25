from collections import defaultdict

def solution(id_list, report, k):
    
    report_list = {}#defaultdict(set)
    
    for rep in report:
        a,b = rep.split()
        if b in report_list:
            report_list[b].add(a)
        else:
            report_list[b] = set()
            report_list[b].add(a)
    
    mail_list = {}
    
    for reported_user in report_list:
        if len(report_list[reported_user]) >= k:
            for reporter in report_list[reported_user]:
                if reporter in mail_list:
                    mail_list[reporter] += 1
                else:
                    mail_list[reporter] = 1
                    
                    
    answer = []            
    for i in id_list:
        if i in mail_list:
            answer.append(mail_list[i])
        else:
            answer.append(0)
    
    
    
    return answer
# Розвробка мікросервісів
# Лабораторна работа #1 
# Тема: Розгортання додатку в середовищі Kubernetes
## Виконав студент групи IO-06 Остапенко Богдан
### Завдання:

1. Створити кластер *Kubernetes*.
2. Реалізувати кілька сервісів (1 сервіс на студента + клієнт). Описати для них *Dockerfile*.
3. Розгорнути сервіси в середовищі *Kubernetes*.
4. Реалізувати доступ до сервісів за допомогою *Ingress*.

# 1.
Так як я використовую windows, я використав команду:

```shell
minikube start --driver=hyperv
```
Ще я помітив, що при виконанні команди без vpn, в мене не працює api та kubernetes.

За допомогою команди *minikube status* я можу впевнитись, що minikube кластер працює.

![image](https://user-images.githubusercontent.com/98806855/194111462-17308065-1601-49e0-b1ea-5e19767b6b04.png)

kubectl теж працює.
![image](https://user-images.githubusercontent.com/98806855/194111760-c1501e6e-99e3-49d5-9072-c40122401a04.png)

# 2. 
Сервіс я розробив на python, за допомогою фреймворку FastAPI.
Сервіс дозволяє створювати списки вигляду: ["предмет", "ціна"], та дивитись, на них.

![image](https://user-images.githubusercontent.com/98806855/194115363-80d23c52-d078-4aa2-8711-7983aaf7d6c2.png)
![image](https://user-images.githubusercontent.com/98806855/194115404-63c4771a-4b87-48fb-9271-c7d2782aabc5.png)
![image](https://user-images.githubusercontent.com/98806855/194115481-d166f030-9bde-4f6d-9c18-15a5b2688673.png)

Для того щоб контенерейзувати сервіс, я написав файл requirement.txt, з усіма библиотеками, які використовуються у проекті.
Також я описав dockerfile, який розгортує сервіс.
# 3 
Образ докер я створив за допомогою команди:
```shell
docker build -t bra1let/somepy:0.1 -f Dokerfile .
```
Після цього я описав deployment.yaml та service.yaml.
Замість ClusterIP, використовував NodePort.
За допомогою команди *minikube service list*, я дізнавася посилання на сервіс.
![image](https://user-images.githubusercontent.com/98806855/194117340-c401f18f-f794-4fe3-aefc-6a6aaa83d2f6.png)
![image](https://user-images.githubusercontent.com/98806855/194117435-807dc3ab-1e17-48cd-9e03-7592a5f448dd.png)
Сервіс працює за цим посиланням.
# 4 
Після опису файлу ingress.yaml, я замінив у файлі service.yaml NodePort на ClusterIP, та скористався командами:
```shell
kubectl delete -f .\k8s\serviceitem\
```
```shell
kubectl apply -f .\k8s\serviceitem\
```
Далі ввів команду *minikube ip*, та перейшов по посиланню:
![image](https://user-images.githubusercontent.com/98806855/194117921-357b6bba-84ab-4c85-8883-0a6a23e61037.png)
(minikube ip)/api/service
Після цього я стикнувся з проблемою, побачивши таку сторінку:
![image](https://user-images.githubusercontent.com/98806855/194118233-d9f828b5-198b-4f08-9348-815a5a32f518.png)
Потрібно було змінити посилання у сервісі, але легше було скоротити посилання до '/', у файлі ingress.yaml.
Сервіс вдалось розгорнути, та він працює.

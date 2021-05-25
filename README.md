# k8s_istio
Configure k8s with istio

1. Для использования возможностей `istio` после разввертывания текущих конфигураций 
разрешаем в созданом неймспейсе автоматическое создание сайдеркаров:

`kubectl label namespace ng1 istio-injection=enabled`

2. Для создания сайдеркаров необходимо пересоздать контейнеры, используем скейл:

`kubectl -n ng scale deployment ng-deployment-v1 --replicas=0`
`kubectl -n ng scale deployment ng-deployment-v1 --replicas=1`

3. Проверяем количество созданых подов (должно быть 2)

`kubectl get pods -n ng`

4. Можем посмотреть в `kiali`

`istioctl dashboard kiali`

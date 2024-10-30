# Cliente de Localização

Este projeto é um aplicativo Android que obtém a localização do dispositivo periodicamente, 
mesmo quando o aplicativo está fechado, e exibe uma notificação com a localização atual.


## Funcionalidades

- **Localização em Tempo Real:** Obtém a localização atual do dispositivo assim que o app inicia.
- **Permissões de Localização:** Solicita permissões de localização em primeiro plano e em segundo plano (para dispositivos Android 10 ou superior).
- **Execução em Segundo Plano:** Usa o `WorkManager` para executar tarefas periódicas a cada 15 minutos.
- **Notificações:** Exibe notificações com a localização atual do dispositivo, mesmo que o app esteja minimizado ou fechado.
- **Suporte para Diferentes Versões do Android:** Compatível com a permissão de localização em segundo plano no Android 10 (API 29) ou superior.

## Bibliotecas Utilizadas

- **Jetpack Compose:** Construção de UI de forma declarativa.
- **Google Play Services Location:** Obtenção da localização do dispositivo.
- **WorkManager:** Agendamento e gerenciamento de tarefas em segundo plano.
- **Kotlin Coroutines:** Suporte para operações assíncronas.

## Dependências

No arquivo `build.gradle`, inclua as seguintes dependências:

```gradle
dependencies {
    implementation "com.google.android.gms:play-services-location:21.0.1"
    implementation "androidx.work:work-runtime-ktx:2.7.1"
    implementation "org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.6.0"
}

```

## Estrutura do Código

- **MainActivity:** Inicializa o cliente de localização e define o conteúdo da tela com o Jetpack Compose.
- **LocationApp:** componente que pode ser composto que solicita permissões de localização e exibe a localização atual do dispositivo.
- **LocationWorker:** Worker executado periodicamente para obter a localização e exibir uma notificação com os dados atuais.
- **Funções Auxiliares:**
    + **getCurrentLocation:** Obtém a última localização conhecida do dispositivo.
    + **createNotificationChannel:** Cria o canal de notificação para dispositivos com Android O (API 26) ou superior.
    + **showLocationNotification:** Exibe uma notificação com a localização.

## Permissões

### No AndroidManifest.xml, adicione as seguintes permissões para que o aplicativo funcione corretamente:

```

<!-- Permissão para acessar a localização em primeiro plano -->
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

<!-- Permissão para acessar a localização em segundo plano (Android 10 ou superior) -->
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />

<!-- Permissão para localização aproximada, se necessário -->
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />


<!-- Permissão para evitar que o app seja encerrado em segundo plano -->
<uses-permission android:name="android.permission.FOREGROUND_SERVICE" />

<!-- Permissão para exibir notificações -->
<uses-permission android:name="android.permission.ACCESS_NOTIFICATION_POLICY" />

```


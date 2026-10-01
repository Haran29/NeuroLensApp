# NeuroLens Frontend

Expo + React Native client for NeuroLens.

## Run locally

```bash
npm install
npm start
```

Additional scripts:

```bash
npm run android
npm run ios
npm run web
npm run lint
npm run build
```

## Configuration

Set this environment variable when the app should call a different backend URL:

- `EXPO_PUBLIC_API_BASE_URL`

Example:

```bash
EXPO_PUBLIC_API_BASE_URL=http://192.168.1.100:8000 npx expo start
```

If not provided, the app falls back to the default base URL in `constants/api.ts`.

## Key directories

- `app/` – screens/routes (Expo Router)
- `components/` – shared UI pieces
- `contexts/` – auth, language, and assessment state
- `services/` – API/service integrations
- `locales/` – i18n dictionaries

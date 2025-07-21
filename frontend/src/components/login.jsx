import React, { useState } from 'react';

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await fetch('http://localhost:8000/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (res.ok) {
        const data = await res.json();
        if (data.status === 'ok') {
          setMessage('Inicio de sesión exitoso');
          // Aquí puedes redirigir o cambiar estado para mostrar dashboard
        } else {
          setMessage('Usuario o contraseña incorrectos');
        }
      } else {
        setMessage('Error en la autenticación');
      }
    } catch (error) {
      setMessage('Error de conexión con el servidor');
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Login</h1>
      {message && <p>{message}</p>}
      <form onSubmit={handleLogin}>
        <label>
          Usuario:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label><br/>
        <label>
          Contraseña:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label><br/>
        <button type="submit">Entrar</button>
      </form>
    </div>
  );
}

export default Login;

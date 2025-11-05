import React from 'react';
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  TextField,
  MenuItem,
  Alert,
} from '@mui/material';
import { endpoints } from '../api';

export default function CreateEntityDialog({ open, type, onClose }) {
  const [formData, setFormData] = React.useState({});
  const [error, setError] = React.useState('');
  const [municipios, setMunicipios] = React.useState([]);

  React.useEffect(() => {
    if (type === 'territorio') {
      fetchMunicipios();
    }
  }, [type]);

  const fetchMunicipios = async () => {
    try {
      const response = await municipiosApi.getAll();
      setMunicipios(response.data);
    } catch (error) {
      console.error('Error al obtener municipios:', error);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
      switch (type) {
        case 'user':
          await authApi.register({ ...formData, role: 'user' });
          break;
        case 'municipio':
          await municipiosApi.create(formData);
          break;
        case 'territorio':
          await territoriosApi.create(formData);
          break;
      }
      onClose();
      setFormData({});
      setError('');
    } catch (error) {
      setError(error.response?.data?.detail || 'Error al crear');
    }
  };

  return (
    <Dialog open={open} onClose={onClose}>
      <DialogTitle>
        {type === 'user' && 'Crear Usuario'}
        {type === 'municipio' && 'Crear Municipio'}
        {type === 'territorio' && 'Crear Territorio'}
      </DialogTitle>
      <DialogContent>
        {error && (
          <Alert severity="error" sx={{ mb: 2 }}>
            {error}
          </Alert>
        )}
        {type === 'user' && (
          <>
            <TextField
              autoFocus
              margin="dense"
              name="email"
              label="Correo Electrónico"
              type="email"
              fullWidth
              variant="outlined"
              value={formData.email || ''}
              onChange={handleChange}
            />
            <TextField
              margin="dense"
              name="password"
              label="Contraseña"
              type="password"
              fullWidth
              variant="outlined"
              value={formData.password || ''}
              onChange={handleChange}
            />
          </>
        )}
        {type === 'municipio' && (
          <TextField
            autoFocus
            margin="dense"
            name="name"
            label="Nombre del Municipio"
            fullWidth
            variant="outlined"
            value={formData.name || ''}
            onChange={handleChange}
          />
        )}
        {type === 'territorio' && (
          <>
            <TextField
              autoFocus
              margin="dense"
              name="name"
              label="Nombre del Territorio"
              fullWidth
              variant="outlined"
              value={formData.name || ''}
              onChange={handleChange}
            />
            <TextField
              select
              margin="dense"
              name="municipio_id"
              label="Municipio"
              fullWidth
              variant="outlined"
              value={formData.municipio_id || ''}
              onChange={handleChange}
            >
              {municipios.map((municipio) => (
                <MenuItem key={municipio.id} value={municipio.id}>
                  {municipio.name}
                </MenuItem>
              ))}
            </TextField>
          </>
        )}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancelar</Button>
        <Button onClick={handleSubmit} variant="contained">
          Crear
        </Button>
      </DialogActions>
    </Dialog>
  );
}
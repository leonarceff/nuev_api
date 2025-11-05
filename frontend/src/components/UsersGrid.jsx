import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Box, Alert, Snackbar } from '@mui/material';
import { endpoints } from '../api';

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  { field: 'email', headerName: 'Correo', width: 200 },
  { field: 'role', headerName: 'Rol', width: 130 },
];

export default function UsersGrid() {
  const [users, setUsers] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(null);

  const fetchUsers = async () => {
    try {
      setLoading(true);
      const response = await endpoints.users.getAll();
      setUsers(response.data);
      setError(null);
    } catch (err) {
      console.error('Error al obtener usuarios:', err);
      setError('Error al cargar los usuarios. Por favor, intente nuevamente.');
    } finally {
      setLoading(false);
    }
  };

  React.useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={users}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        disableSelectionOnClick
        loading={loading}
        autoHeight
      />
      <Snackbar 
        open={!!error} 
        autoHideDuration={6000} 
        onClose={() => setError(null)}
      >
        <Alert onClose={() => setError(null)} severity="error" sx={{ width: '100%' }}>
          {error}
        </Alert>
      </Snackbar>
    </Box>
  );
}
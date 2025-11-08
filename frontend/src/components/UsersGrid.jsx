import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Box, Alert } from '@mui/material';
import { usersApi } from '../api';

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  { field: 'email', headerName: 'Correo', width: 250 },
  { field: 'role', headerName: 'Rol', width: 130 },
];

export default function UsersGrid() {
  const [users, setUsers] = React.useState([]);
  const [loading, setLoading] = React.useState(true);
  const [error, setError] = React.useState(null);

  const fetchUsers = async () => {
    try {
      const response = await usersApi.getAll();
      // Asegurarse de que cada usuario tenga un ID
      const usersWithId = Array.isArray(response.data) ? response.data.map(user => ({
        ...user,
        id: user.id || Math.random() // Fallback en caso de que no venga el ID
      })) : [];
      setUsers(usersWithId);
      setError(null);
    } catch (error) {
      console.error('Error al obtener usuarios:', error);
      setError(error.response?.data?.detail || 'Error al cargar los usuarios');
    } finally {
      setLoading(false);
    }
  };

  React.useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      {error && (
        <Alert severity="error" sx={{ mb: 2 }}>
          {error}
        </Alert>
      )}
      <DataGrid
        rows={users}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: { pageSize: 5 }
          }
        }}
        pageSizeOptions={[5, 10, 25]}
        disableRowSelectionOnClick
        loading={loading}
        autoHeight
      />
    </Box>
  );
}
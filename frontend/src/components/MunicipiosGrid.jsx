import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Box } from '@mui/material';
import { municipiosApi } from '../api';

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  { field: 'name', headerName: 'Nombre', width: 200 },
];

export default function MunicipiosGrid() {
  const [municipios, setMunicipios] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  const fetchMunicipios = async () => {
    try {
      const response = await municipiosApi.getAll();
      setMunicipios(response.data);
    } catch (error) {
      console.error('Error al obtener municipios:', error);
    } finally {
      setLoading(false);
    }
  };

  React.useEffect(() => {
    fetchMunicipios();
  }, []);

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={municipios}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        disableSelectionOnClick
        loading={loading}
      />
    </Box>
  );
}
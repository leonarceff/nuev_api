import React from 'react';
import { DataGrid } from '@mui/x-data-grid';
import { Box } from '@mui/material';
import { territoriosApi } from '../api';

const columns = [
  { field: 'id', headerName: 'ID', width: 90 },
  { field: 'name', headerName: 'Nombre', width: 200 },
  { field: 'municipio_name', headerName: 'Municipio', width: 200 },
];

export default function TerritoriosGrid() {
  const [territorios, setTerritorios] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  const fetchTerritorios = async () => {
    try {
      const response = await territoriosApi.getAll();
      setTerritorios(response.data);
    } catch (error) {
      console.error('Error al obtener territorios:', error);
    } finally {
      setLoading(false);
    }
  };

  React.useEffect(() => {
    fetchTerritorios();
  }, []);

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={territorios}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        disableSelectionOnClick
        loading={loading}
      />
    </Box>
  );
}
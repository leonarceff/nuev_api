import React from 'react';
import {
  Button,
  Container,
  Typography,
  Box,
  AppBar,
  Toolbar,
  IconButton,
  Menu,
  MenuItem,
} from '@mui/material';
import AccountCircle from '@mui/icons-material/AccountCircle';
import { useNavigate } from 'react-router-dom';
import UsersGrid from '../components/UsersGrid';
import MunicipiosGrid from '../components/MunicipiosGrid';
import TerritoriosGrid from '../components/TerritoriosGrid';
import CreateEntityDialog from '../components/CreateEntityDialog';

export default function AdminPage() {
  const navigate = useNavigate();
  const [anchorEl, setAnchorEl] = React.useState(null);
  const [openDialog, setOpenDialog] = React.useState(false);
  const [dialogType, setDialogType] = React.useState(null);

  const handleMenu = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  const handleCreateClick = (type) => {
    setDialogType(type);
    setOpenDialog(true);
  };

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            Panel de Administración
          </Typography>
          <IconButton
            size="large"
            aria-label="cuenta del usuario"
            aria-controls="menu-appbar"
            aria-haspopup="true"
            onClick={handleMenu}
            color="inherit"
          >
            <AccountCircle />
          </IconButton>
          <Menu
            id="menu-appbar"
            anchorEl={anchorEl}
            anchorOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
            keepMounted
            transformOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
            open={Boolean(anchorEl)}
            onClose={handleClose}
          >
            <MenuItem onClick={handleLogout}>Cerrar Sesión</MenuItem>
          </Menu>
        </Toolbar>
      </AppBar>

      <Container sx={{ mt: 4 }}>
        <Box sx={{ mb: 4 }}>
          <Button
            variant="contained"
            onClick={() => handleCreateClick('user')}
            sx={{ mr: 2 }}
          >
            Crear Usuario
          </Button>
          <Button
            variant="contained"
            onClick={() => handleCreateClick('municipio')}
            sx={{ mr: 2 }}
          >
            Crear Municipio
          </Button>
          <Button
            variant="contained"
            onClick={() => handleCreateClick('territorio')}
          >
            Crear Territorio
          </Button>
        </Box>

        <Typography variant="h5" sx={{ mt: 4, mb: 2 }}>
          Usuarios
        </Typography>
        <UsersGrid />

        <Typography variant="h5" sx={{ mt: 4, mb: 2 }}>
          Municipios
        </Typography>
        <MunicipiosGrid />

        <Typography variant="h5" sx={{ mt: 4, mb: 2 }}>
          Territorios
        </Typography>
        <TerritoriosGrid />
      </Container>

      <CreateEntityDialog
        open={openDialog}
        type={dialogType}
        onClose={() => setOpenDialog(false)}
      />
    </Box>
  );
}
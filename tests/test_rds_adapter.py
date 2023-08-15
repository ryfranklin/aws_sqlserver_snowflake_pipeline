from unittest.mock import patch, MagicMock
from interface_adapters.rds_adapter import RDSAdapter


class TestRDSAdapter:

    @patch('boto3.Session.client')
    def test_init(self, mock_client):
        mock_session = MagicMock()
        rds = RDSAdapter(mock_session)
        mock_session.client.assert_called_once_with('rds')
        assert rds.rds == mock_session.client.return_value

    @patch.object(RDSAdapter, 'create_instance')
    def test_create_instance(self, mock_create_instance):
        mock_create_instance.return_value = 'mock_instance'
        rds = RDSAdapter(MagicMock())
        instance = rds.create_instance("test_id",
                                       "test_user",
                                       "test_pass",
                                       "sqlserver",
                                       20
                                       )
        mock_create_instance.assert_called_once_with("test_id",
                                                     "test_user",
                                                     "test_pass",
                                                     "sqlserver",
                                                     20
                                                     )
        assert instance == 'mock_instance'

    @patch.object(RDSAdapter, 'delete_instance')
    def test_delete_instance(self, mock_delete_instance):
        mock_delete_instance.return_value = 'mock_delete_response'
        rds = RDSAdapter(MagicMock())
        response = rds.delete_instance("test_id", True)
        mock_delete_instance.assert_called_once_with("test_id", True)
        assert response == 'mock_delete_response'

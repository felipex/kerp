# app/test_validators.py
import pytest
from django.core.exceptions import ValidationError
from core.models.validators import validate_cpf, format_cpf, validate_cnpj, format_cnpj


class TestCPFValidation:
    """Tests for CPF validation logic"""

    def test_valid_cpf(self):
        """Test a known valid CPF"""
        valid_cpf = "12345678909"
        # Should not raise exception
        validate_cpf(valid_cpf)  # If invalid, pytest fails automatically

    def test_invalid_cpf_length(self):
        """Test CPF with wrong length"""
        with pytest.raises(ValidationError):
            validate_cpf("123456789")

    def test_invalid_cpf_checksum(self):
        """Test CPF with wrong check digits"""
        with pytest.raises(ValidationError):
            validate_cpf("12345678900")

    def test_sequential_digits(self):
        """Test CPF with all same digits"""
        with pytest.raises(ValidationError):
            validate_cpf("11111111111")

    def test_formatted_input(self):
        """Test validator accepts formatted CPF"""
        validate_cpf("123.456.789-09")  # Should not raise

    def test_format_cpf_helper(self):
        """Test formatting helper function"""
        raw = "12345678909"
        formatted = format_cpf(raw)
        assert formatted == "123.456.789-09"

    @pytest.mark.parametrize("invalid_cpf", [
        "00000000000",
        "11111111111",
        "22222222222",
        "1234567890",  # Too short
        "123456789091",  # Too long
        "abc12345678",  # Invalid chars
    ])
    def test_multiple_invalid_cpfs(self, invalid_cpf):
        """Parametrized test for multiple invalid CPFs"""
        with pytest.raises(ValidationError):
            validate_cpf(invalid_cpf)


class TestCNPJValidation:
    """Tests for CNPJ validation logic"""

    def test_valid_cnpj(self):
        """Test a known valid CNPJ"""
        valid_cnpj = "18621825000199"
        # Should not raise exception
        validate_cnpj(valid_cnpj)  # If invalid, pytest fails automatically

    def test_invalid_cnpj_length(self):
        """Test CNPJ with wrong length"""
        with pytest.raises(ValidationError):
            validate_cnpj("1234567800019")

    def test_invalid_cnpj_checksum(self):
        """Test CNPJ with wrong check digits"""
        with pytest.raises(ValidationError):
            validate_cnpj("12345678000191")

    def test_sequential_digits(self):
        """Test CNPJ with all same digits"""
        with pytest.raises(ValidationError):
            validate_cnpj("11111111111111")

    def test_formatted_input(self):
        """Test validator accepts formatted CNPJ"""
        validate_cnpj("53.619.181/0001-03")  # Should not raise

    def test_format_cnpj_helper(self):
        """Test formatting helper function"""
        raw = "12345678000190"
        formatted = format_cnpj(raw)
        assert formatted == "12.345.678/0001-90"

    @pytest.mark.parametrize("invalid_cnpj", [
        "00000000000000",
        "11111111111111",
        "22222222222222",
        "1234567800019",  # Too short
        "123456780001901",  # Too long
        "abc123456780001",  # Invalid chars
    ])
    def test_multiple_invalid_cnpjs(self, invalid_cnpj):
        """Parametrized test for multiple invalid CNPJs"""
        with pytest.raises(ValidationError):
            validate_cnpj(invalid_cnpj)
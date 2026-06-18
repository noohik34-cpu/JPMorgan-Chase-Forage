def price_gas_contract(
    injection_price,
    withdrawal_price,
    volume,
    storage_cost
):
    """
    Calculate the value of a natural gas storage contract.
    """

    purchase_cost = injection_price * volume
    sale_revenue = withdrawal_price * volume

    contract_value = (
        sale_revenue
        - purchase_cost
        - storage_cost
    )

    return contract_value


# Sample Test Case

contract_value = price_gas_contract(
    injection_price=10.0,
    withdrawal_price=12.5,
    volume=1000000,
    storage_cost=50000
)

print("Contract Value =", contract_value)

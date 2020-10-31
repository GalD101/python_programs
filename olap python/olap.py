from olapy.core.mdx.executor import MdxEngine
executor = MdxEngine()  # instantiate the MdxEngine
# executor.load_cube('Analysis Services Tutorial.cube')  # load sales cube
print(executor.execute_mdx("""
SELECT
Hierarchize({[Measures].[Amount]}) ON COLUMNS
""")['result'])
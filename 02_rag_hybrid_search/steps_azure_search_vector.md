# Step 1: Create a Storage account, and add your container
# Step 2: Create your azure AI search (search service)
# Step 3: Enable system assigned from identity in azure search service
# Step 4: Setup forundy deploy model
# Step 5: add role assignetn in foundry 
add cognitive Services openai user role for openai search
add role assignment (Storage Blob Data Contributor) role in the storage account that we stored our pdf
- Both assigned to your search service AZURE OPENAI
- Deploy embedding (text-embedding -3-small and another one model)
now add index from search service
for vector embedding (semantic)
add new index add searchable add dimension according to your embedding 1536 for text embedding small  make it searchable add algorithm, vectorizer and a algorithm, 
Vectorizer -> kind will be azure ai foundry(preview)
We don't need compressor

(JSON)
Add skillset ->  mergeskill, aiembeddingskill

Update Indexer -> Output mapping

## Adding vector for similarity search
Steps: 
add a field in your index (azure ai search)
Field Name: Name
type: Collection(Edm.Single)
Dimension: How much data can be stored
Microsoft support dimension by modelName 
1536

RBAC For Azure foundry
Add Role assignment-( Cognitive Services OpenAI user)
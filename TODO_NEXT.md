# TODO Next

## Immediate — Phase 1 Foundation

### Backend-Core Session
1. [x] Create `apps/` directory and all seven app packages with `__init__.py`
2. [x] Create custom User model in `accounts` (extend AbstractUser) — BEFORE any migrate
3. [x] Update `settings.py`: add all apps to INSTALLED_APPS, set AUTH_USER_MODEL, configure static/media
4. [x] Create `core` base models: TimestampedModel, SlugModel
5. [x] Create `catalog` models: Category, WebTemplate, TemplateAsset, TemplateBrand, Tag
6. [x] Register all models in Django admin with useful list displays and filters
7. [x] Create `requirements.txt` pinning key dependencies
8. [x] Run `makemigrations` and `migrate` — verify clean migration
9. [x] Create initial data fixtures or management command for MVP categories
10. [x] Set up basic URL routing skeleton across all apps

### Premium-UI Session
1. [ ] Create `templates/base.html` master template with Bootstrap 5 CDN/local
2. [ ] Design and implement the SCSS design system (colors, typography, spacing variables)
3. [ ] Create premium navigation component (header + mobile menu)
4. [ ] Create premium footer component
5. [ ] Build homepage skeleton with hero section, featured categories, featured templates
6. [ ] Build category listing page template
7. [ ] Build template detail page template
8. [ ] Build premium card component for template listings
9. [ ] Set up `static/` directory structure
10. [ ] Ensure RTL-ready class structure from the start

## Next — Phase 2 (after Phase 1 complete)

### Backend-Core
- [ ] Editor app models: EditableRegion, RegionType
- [ ] Projects app models: CustomerProject (with UUID), ProjectRevision, ProjectContent
- [ ] Commerce app models: PricePlan, Order, OrderItem, License
- [ ] DRF API endpoints for catalog (list, detail, filter)
- [ ] DRF API endpoints for editor save/load
- [ ] User authentication views (register, login, dashboard)
- [ ] Catalog selectors: featured templates, by category, by tag
- [ ] Catalog services: template CRUD operations

### Premium-UI
- [ ] Template preview system (iframe or server-rendered)
- [ ] Editor app basic UI
- [ ] User authentication pages (login, register, password reset)
- [ ] User dashboard page
- [ ] Cart and checkout page skeletons

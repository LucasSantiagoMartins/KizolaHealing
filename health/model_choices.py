INSTITUTION_TYPE = (
    ('HPG', 'Hospital Geral'),
    ('HED', 'Hospital Especializado'),
        ('HCG',' Hospital de Cardiologia'),
        ('HOG', 'Hospital de Oncologia '),
        ('HPC',' Hospital Psiquiátrico'),
        ('HTP', 'Hospital Ortopédico'),
        ('HPA', 'Hospital Pediátrico'),
        ('HFG', 'Hospital Oftalmológico'),
        ('HNG', 'Hospital de Neurologia'),
        ('HUT', 'Hospital Universitário '),
        ('HRB', 'Hospital de Reabilitação'),
        ('HUE', 'Hospital de Urgência e Emergência'),
        ('HMD', 'Hospital Maternidade'),
        ('HCA', 'Hospital de Cirurgia'),
        ('HDI', 'Hospital de Doenças Infecciosas'),
    ('HMT', 'Hospital Militar'),
    ('HCT', 'Hospital Comunitário'),
    ('HLP', 'Hospital de Longa Permanência'),
    ('CGL', 'Clínica Geral'),
    ('CED', 'Clínica Especializada'),
        ('CCG', 'Clínica de Cardiologia:'),
        ('CDG', 'Clínica de Dermatologia:'),
        ('CGO', 'Clínica de Ginecologia e Obstetrícia'),
        ('COP', 'Clínica de Ortopedia'),
        ('CPT', 'Clínica de Pediatria'),
        ('CNG', 'Clínica de Neurologia'),
        ('COG', 'Clínica de Oftalmologia'),
        ('CEG', 'Clínica de Endocrinologia'),
        ('CPQ', 'Clínica de Psiquiatria'),
    ('CTG', 'Clínica Odontológica'),
    ('CFP', 'Clínica de Fisioterapia'),
    ('CET', 'Clínica de Estética'),
    ('CIM', 'Clínica de Imagem'),
    ('CMT', 'Clínica de Medicina do Trabalho'),
    ('CFD', 'Clínica de Fertilidade'),
    ('CRB', 'Clínica de Reabilitação'),
    ('CHS', 'Clínica de Hemodiálise'),
    ('COA', 'Clínica de Oncologia'),
    ('CVT', 'Clínica Veterinária'),
    ('CPL', 'Clínica Popular'),
)

PHONE_TYPES = (
    ('TFP', 'Telefone Principal'),
    ('TFE', 'Telefone de Emergência'),
    ('TFR', 'Telefone de Recepção'),
    ('TAP', 'Telefone de Atendimento ao Paciente'),
    ('TFC', 'Telefone de Consultório'),
    ('TUI', 'Telefone de Unidade de Internação'),
    ('TFL', 'Telefone de Laboratório'),
    ('TFF', 'Telefone de Farmácia'),
    ('TFA', 'Telefone de Administração'),
    ('TRH', 'Telefone de Departamento de Recursos Humanos'),
    ('TST', 'Telefone de Suporte Técnico'),
)

SERVICE_TYPE_CHOICES = (
    ('CTM', 'Consultas Médicas'),
    ('SDG', 'Serviços de Diagnóstico'),
    ('SCG', 'Serviços Cirúgicos'),
    ('SUE', 'Serviços de Urgência e Emergência'),
    ('SVI', 'Serviços de Internação'),
    ('SVR', 'Serviços de Reabilitação'),
    ('SSP', 'Serviços de Saúde Preventiva'),
    ('SSM', 'Serviços de Saúde Mental'),
    ('SVO', 'Serviços de Odontologia'),
)

POLICY_TITLE_CHOICES = (
    ('PPD', 'Política de Privacidade '),
    ('PRD', 'Política de Retenção de Dados'),
    ('DRP', 'Direitos e Responsabilidades do Paciente '),
    ('PFP', 'Política de Faturamento e Pagamento '),
    ('PVT', 'Política de Visitantes '),
    ('PMT', 'Política de Medicamentos'),
    ('PCI', 'Política de Controle de Infecções'),
    ('PSE', 'Política de Segurança e Emergências '),
    ('PSO', 'Política de Saúde e Segurança Ocupacional '),
    ('PSI', 'Política de Consentimento Informado '),
    ('PRM', 'Política de Requisitos de Documentação Médica'),
    ('PPP', 'Política de Proteção de Dados Pessoais '),
    ('PEM', 'Política de Uso de Equipamentos Médicos '),
    ('PAP', 'Política de Atendimento e Cuidados ao Paciente'),
    ('PDR', 'Política de Descarte de Resíduos '),
    ('PAD', 'Política de Acessibilidade '),
    ('PTD', 'Política de Treinamento e Desenvolvimento'),
    ('PGR', 'Política de Gestão de Riscos '),
    ('PTI', 'Política de Conflitos de Interesse '),
    ('PTC', 'Política de Transparência'),
)

LICENSE_TITLE_CHOICES = (
    ('LCF', 'licença de funcionamento'),
    ('RER', 'registro na entidade reguladora'),
    ('LCS', 'licença sanitária'),
    ('ALM', 'alavará de licença municipal'),
    ('LEM', 'licenças para especialidades médicas'),
)

CERTIFICATION_TITLE_CHOICES = (
    ('CCI', 'certificações em controle de infecção'),
    ('CPF', 'certificados profissionais para funcionarios'),
    ('CAH', 'acreditação hospitalar'),
    ('CEQ', 'certificações específicas de qualidade'),
    ('CQP', 'certificações de qualidade e boas práticas'),
    
)

STATUS_CHOICES = (
    ('ATV', 'Activa'),
    ('EXD', 'Expirada'),
    ('SPC', 'Suspença'),
)

OPERATING_HOURS_CHOICES = (
    ('HRC', 'Horário Comercial'),
    ('HRE', 'Horário Estendido'),
    ('HRN', 'Horário Noturno'),
    ('24H', '24 Horas'),
    ('HMP', 'Meio Período'),
    ('HDA', 'Dias Alternados'),
    ('HRP', 'Horário de Ponto'),
    ('HAE', 'Atendimento de Emergência'),
    ('HFE', 'Atendimento Fora do Expediente'),
    ('HCE', 'Horário para Consultas Específicas'),
    ('HRF', 'Horário Flexível'),
    ('HAA', 'Atendimento por Agendamento'),
    ('HRR', 'Horário Reduzido'),
    ('HRT', 'Horário Temporário'),
    ('HPN', 'Horário de Plantão'),
    ('HRV', 'Horário Rotativo'),
    ('HPE', 'Horário Especial para Pacientes Específicos'),
    ('HET', 'Horário Exclusivo de Telemedicina'),
    ('HCA', 'Horário de Consultas Ambulatoriais'),
    ('HCG', 'Horário para Consultas gerais'),
    ('HEC', 'Horário para Consultas especializadas'),
)
